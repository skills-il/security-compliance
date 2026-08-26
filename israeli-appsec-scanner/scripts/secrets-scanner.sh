#!/usr/bin/env bash
# ============================================================================
# Israeli Service Credentials Scanner
# Scans a project directory for leaked Israeli service credentials,
# API keys, and sensitive configuration values.
#
# Usage:
#   bash secrets-scanner.sh /path/to/project
#   bash secrets-scanner.sh /path/to/project --json
#   bash secrets-scanner.sh /path/to/project --verbose
# ============================================================================

set -euo pipefail

# Colors for terminal output
RED='\033[0;31m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
PROJECT_DIR="${1:-.}"
OUTPUT_FORMAT="text"
VERBOSE=false
FINDINGS=0
CRITICAL_FINDINGS=0

for arg in "$@"; do
    case "$arg" in
        --json) OUTPUT_FORMAT="json" ;;
        --verbose) VERBOSE=true ;;
    esac
done

if [ ! -d "$PROJECT_DIR" ]; then
    echo "Error: '$PROJECT_DIR' is not a valid directory." >&2
    exit 1
fi

# Resolve to absolute path
PROJECT_DIR="$(cd "$PROJECT_DIR" && pwd)"

# ---------------------------------------------------------------------------
# Patterns for Israeli service credentials
# ---------------------------------------------------------------------------
# Patterns are written as POSIX extended regular expressions (ERE), not PCRE.
# BSD/macOS grep has no -P, and the previous PCRE patterns combined with
# "|| true" made the scanner report a clean project on macOS no matter what was
# leaked. ERE + "grep -iE" works identically on GNU and BSD grep.
#
# Portability note: bash 3.2 (the /bin/bash macOS still ships) has no
# associative arrays, so patterns are held in two parallel indexed arrays.
Q="[\"']"                 # a quote character
SP="[[:space:]]"          # whitespace, standalone
SPC="[:space:]"           # whitespace CLASS, for use inside a bracket expression
D="[0-9]"                 # digit
AN="[a-zA-Z0-9]"          # alphanumeric

PATTERN_NAMES=()
PATTERN_REGEXES=()
PATTERN_SEVERITIES=()

add_pattern() {
    PATTERN_NAMES+=("$1")
    PATTERN_REGEXES+=("$2")
    PATTERN_SEVERITIES+=("$3")
}

# Israeli Payment Gateways
add_pattern "Cardcom Terminal Number" "(cardcom|terminal)[_${SPC}]*[=:]${SP}*${Q}?${D}{6,8}${Q}?" "CRITICAL"
add_pattern "Tranzila Supplier Code" "(tranzila|supplier)[_${SPC}]*[=:]${SP}*${Q}?${AN}{4,20}${Q}?" "CRITICAL"
add_pattern "PayMe Seller ID" "(payme|seller[_${SPC}]?id)[_${SPC}]*[=:]${SP}*${Q}?[a-zA-Z0-9-]{8,}${Q}?" "CRITICAL"
add_pattern "Meshulam API Key" "(meshulam|page[_${SPC}]?code)[_${SPC}]*[=:]${SP}*${Q}?${AN}{6,}${Q}?" "CRITICAL"

# Israeli SMS Gateways
add_pattern "Cellact API Key" "cellact[_${SPC}-]*(api|key|token|secret)[_${SPC}]*[=:]${SP}*${Q}?${AN}{16,}${Q}?" "CRITICAL"
add_pattern "InforUMobile API Key" "(inforu|informobile)[_${SPC}-]*(api|key|token)[_${SPC}]*[=:]${SP}*${Q}?${AN}{16,}${Q}?" "CRITICAL"
add_pattern "019 SMS API Key" "019[_${SPC}-]*(sms|api|key|token)[_${SPC}]*[=:]${SP}*${Q}?${AN}{16,}${Q}?" "CRITICAL"

# Supabase
add_pattern "Supabase Service Role Key" "(supabase|service[_${SPC}-]*role)[_${SPC}-]*(key|secret)[_${SPC}]*[=:]${SP}*${Q}?eyJ[a-zA-Z0-9_-]{20,}${Q}?" "CRITICAL"
add_pattern "Supabase Anon Key (in backend code)" "supabase[_${SPC}-]*anon[_${SPC}-]*(key)[_${SPC}]*[=:]${SP}*${Q}?eyJ[a-zA-Z0-9_-]{20,}${Q}?" "HIGH"

# Israeli Bank APIs
add_pattern "Israeli Bank API Credential" "(poalim|leumi|discount|mizrahi|hapoalim)[_${SPC}-]*(api|key|token|secret|password)[_${SPC}]*[=:]${SP}*${Q}?${AN}{10,}${Q}?" "CRITICAL"

# Government APIs
add_pattern "Gov.il API Token" "(gov\.il|government|misrad)[_${SPC}-]*(api|key|token)[_${SPC}]*[=:]${SP}*${Q}?${AN}{16,}${Q}?" "HIGH"

# Israel Post
add_pattern "Israel Post API Key" "(israel[_${SPC}-]*post|doar[_${SPC}-]*israel)[_${SPC}-]*(api|key|token)[_${SPC}]*[=:]${SP}*${Q}?${AN}{10,}${Q}?" "HIGH"

# Generic sensitive patterns
add_pattern "Hardcoded Password" "(password|passwd|pwd)[_${SPC}]*[=:]${SP}*${Q}[^\"']{3,}${Q}" "HIGH"
add_pattern "Private Key File" "-----BEGIN (RSA |EC |DSA |OPENSSH )?PRIVATE KEY-----" "CRITICAL"
add_pattern "JWT Token (hardcoded)" "eyJ[a-zA-Z0-9_-]{10,}\.eyJ[a-zA-Z0-9_-]{10,}\.[a-zA-Z0-9_-]{10,}" "HIGH"
# Generic credentials. Israeli vendor keys are frequently stored under a plain
# API_KEY / ACCESS_TOKEN name (e.g. INFORU_API_KEY=...), which none of the
# vendor-specific patterns above match, so this catch-all closes that gap.
add_pattern "Generic API Key or Access Token" "(api[_-]?key|api[_-]?secret|access[_-]?token|secret[_-]?key)${SP}*[=:]${SP}*${Q}?${AN}{16,}${Q}?" "HIGH"
add_pattern "Unquoted Password or Secret Assignment" "(password|passwd|pwd|secret)[a-z0-9_.-]*${SP}*=${SP}*[^${SPC}\"'#]" "HIGH"
add_pattern "Prefixed Provider Token" "(sb_secret_|sb_publishable_|ghp_|gho_|ghu_|ghs_|github_pat_|sk_live_|sk_test_|xox[baprs]-|AKIA[0-9A-Z]{16})[A-Za-z0-9_-]{8,}" "CRITICAL"
add_pattern "Israeli ID Number" "(teudat[_${SPC}-]*zehut|israeli?[_${SPC}-]*id|tz[_${SPC}-]*number)[_${SPC}]*[=:]${SP}*${Q}?${D}{9}${Q}?" "HIGH"

# ---------------------------------------------------------------------------
# Directories and files to skip
# ---------------------------------------------------------------------------
SKIP_DIRS=(
    "node_modules" ".git" ".next" "dist" "build" "__pycache__"
    ".venv" "venv" ".cache" "coverage" ".turbo" ".vercel"
)

SKIP_FILES=(
    "*.min.js" "*.min.css" "*.map" "*.lock" "pnpm-lock.yaml"
    "package-lock.json" "yarn.lock" "*.woff" "*.woff2" "*.ttf"
    "*.png" "*.jpg" "*.jpeg" "*.gif" "*.svg" "*.ico"
)

# ---------------------------------------------------------------------------
# Build grep exclude arguments
# ---------------------------------------------------------------------------
EXCLUDE_ARGS=""
for dir in "${SKIP_DIRS[@]}"; do
    EXCLUDE_ARGS="$EXCLUDE_ARGS --exclude-dir=$dir"
done
for file in "${SKIP_FILES[@]}"; do
    EXCLUDE_ARGS="$EXCLUDE_ARGS --exclude=$file"
done

# ---------------------------------------------------------------------------
# Scan functions
# ---------------------------------------------------------------------------
print_header() {
    if [ "$OUTPUT_FORMAT" = "text" ]; then
        echo ""
        echo -e "${CYAN}============================================================${NC}"
        echo -e "${CYAN}  Israeli Service Credentials Scanner${NC}"
        echo -e "${CYAN}  Project: $PROJECT_DIR${NC}"
        echo -e "${CYAN}============================================================${NC}"
        echo ""
    fi
}

scan_pattern() {
    local name="$1"
    local pattern="$2"
    local severity="${3:-HIGH}"

    # POSIX ERE, case-insensitive. Exit status 1 means "no match" and is fine;
    # anything >1 is a real grep failure and must NOT be reported as "clean".
    local results status
    results=$(grep -rnIE -i -e "$pattern" "$PROJECT_DIR" $EXCLUDE_ARGS 2>/dev/null) && status=0 || status=$?
    if [ "$status" -gt 1 ]; then
        echo "ERROR: grep failed (exit $status) while scanning for '$name'." >&2
        echo "       Refusing to report a clean result from a failed scan." >&2
        exit 2
    fi

    if [ -n "$results" ]; then
        while IFS= read -r line; do
            FINDINGS=$((FINDINGS + 1))
            if [ "$severity" = "CRITICAL" ]; then
                CRITICAL_FINDINGS=$((CRITICAL_FINDINGS + 1))
            fi

            if [ "$OUTPUT_FORMAT" = "text" ]; then
                local color="$YELLOW"
                if [ "$severity" = "CRITICAL" ]; then
                    color="$RED"
                fi
                echo -e "${color}[$severity]${NC} $name"
                echo "  $line"
                echo ""
            elif [ "$OUTPUT_FORMAT" = "json" ]; then
                local file_path
                file_path=$(echo "$line" | cut -d: -f1)
                local line_num
                line_num=$(echo "$line" | cut -d: -f2)
                echo "{\"severity\":\"$severity\",\"check\":\"$name\",\"file\":\"$file_path\",\"line\":$line_num}"
            fi
        done <<< "$results"
    elif [ "$VERBOSE" = true ] && [ "$OUTPUT_FORMAT" = "text" ]; then
        echo -e "${GREEN}[PASS]${NC} $name: No findings"
    fi
}

check_env_files() {
    if [ "$OUTPUT_FORMAT" = "text" ]; then
        echo -e "${CYAN}--- Checking for exposed .env files ---${NC}"
        echo ""
    fi

    while IFS= read -r env_file; do
        if [ -z "$env_file" ]; then
            continue
        fi
        # Skip .env.example files
        if [[ "$env_file" == *".env.example"* ]] || [[ "$env_file" == *".env.sample"* ]]; then
            continue
        fi
        # Skip files in excluded directories
        local skip=false
        for dir in "${SKIP_DIRS[@]}"; do
            if [[ "$env_file" == *"/$dir/"* ]]; then
                skip=true
                break
            fi
        done
        if [ "$skip" = true ]; then
            continue
        fi

        FINDINGS=$((FINDINGS + 1))
        CRITICAL_FINDINGS=$((CRITICAL_FINDINGS + 1))

        if [ "$OUTPUT_FORMAT" = "text" ]; then
            echo -e "${RED}[CRITICAL]${NC} Exposed environment file"
            echo "  $env_file"
            echo "  Ensure this file is in .gitignore and not committed."
            echo ""
        elif [ "$OUTPUT_FORMAT" = "json" ]; then
            echo "{\"severity\":\"CRITICAL\",\"check\":\"exposed_env_file\",\"file\":\"$env_file\",\"line\":0}"
        fi
    done < <(find "$PROJECT_DIR" -name ".env*" -type f 2>/dev/null)
}

check_git_history() {
    if [ "$OUTPUT_FORMAT" = "text" ]; then
        echo -e "${CYAN}--- Checking git history for secrets (last 50 commits) ---${NC}"
        echo ""
    fi

    if [ ! -d "$PROJECT_DIR/.git" ]; then
        if [ "$OUTPUT_FORMAT" = "text" ]; then
            echo "  Not a git repository. Skipping history scan."
            echo ""
        fi
        return
    fi

    # Check if any .env files were ever committed
    local env_in_history
    env_in_history=$(cd "$PROJECT_DIR" && git log --all --diff-filter=A --name-only --pretty=format: -n 50 2>/dev/null | grep -E '\.env($|\.)' | head -5 || true)

    if [ -n "$env_in_history" ]; then
        FINDINGS=$((FINDINGS + 1))
        CRITICAL_FINDINGS=$((CRITICAL_FINDINGS + 1))
        if [ "$OUTPUT_FORMAT" = "text" ]; then
            echo -e "${RED}[CRITICAL]${NC} .env files found in git history"
            echo "  The following .env files were committed at some point:"
            echo "$env_in_history" | while IFS= read -r f; do
                echo "    - $f"
            done
            echo "  Consider using 'git filter-repo' or BFG to remove them."
            echo ""
        fi
    elif [ "$VERBOSE" = true ] && [ "$OUTPUT_FORMAT" = "text" ]; then
        echo -e "${GREEN}[PASS]${NC} No .env files found in recent git history"
        echo ""
    fi
}

print_summary() {
    if [ "$OUTPUT_FORMAT" = "text" ]; then
        echo -e "${CYAN}============================================================${NC}"
        echo -e "${CYAN}  Scan Summary${NC}"
        echo -e "${CYAN}============================================================${NC}"
        if [ "$FINDINGS" -eq 0 ]; then
            echo -e "  ${GREEN}No secrets detected.${NC}"
        else
            echo -e "  Total findings: ${YELLOW}$FINDINGS${NC}"
            if [ "$CRITICAL_FINDINGS" -gt 0 ]; then
                echo -e "  Critical findings: ${RED}$CRITICAL_FINDINGS${NC}"
            fi
        fi
        echo ""
        echo "  Note: This scanner uses pattern matching and may produce"
        echo "  false positives. Always verify findings manually."
        echo ""
        echo "  For deeper scanning, consider running:"
        echo "    trufflehog git file://$PROJECT_DIR --only-verified"
        echo "    gitleaks detect --source $PROJECT_DIR --verbose"
        echo -e "${CYAN}============================================================${NC}"
    fi
}

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
print_header

if [ "$OUTPUT_FORMAT" = "text" ]; then
    echo -e "${CYAN}--- Scanning for Israeli service credentials ---${NC}"
    echo ""
fi

# Scan for each pattern
i=0
while [ "$i" -lt "${#PATTERN_NAMES[@]}" ]; do
    scan_pattern "${PATTERN_NAMES[$i]}" "${PATTERN_REGEXES[$i]}" "${PATTERN_SEVERITIES[$i]}"
    i=$((i + 1))
done

# Additional checks
check_env_files
check_git_history

print_summary

# Exit with non-zero if critical findings
if [ "$CRITICAL_FINDINGS" -gt 0 ]; then
    exit 1
fi
