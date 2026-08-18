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
declare -A PATTERNS

# Israeli Payment Gateways
PATTERNS["Cardcom Terminal Number"]='(?i)(cardcom|terminal)[_\s]*[=:]\s*["\x27]?\d{6,8}["\x27]?'
PATTERNS["Tranzila Supplier Code"]='(?i)(tranzila|supplier)[_\s]*[=:]\s*["\x27]?[a-zA-Z0-9]{4,20}["\x27]?'
PATTERNS["PayMe Seller ID"]='(?i)(payme|seller[_\s]?id)[_\s]*[=:]\s*["\x27]?[a-zA-Z0-9-]{8,}["\x27]?'
PATTERNS["Meshulam API Key"]='(?i)(meshulam|page[_\s]?code)[_\s]*[=:]\s*["\x27]?[a-zA-Z0-9]{6,}["\x27]?'

# Israeli SMS Gateways
PATTERNS["Cellact API Key"]='(?i)cellact[_\s-]*(api|key|token|secret)[_\s]*[=:]\s*["\x27]?[a-zA-Z0-9]{16,}["\x27]?'
PATTERNS["InforUMobile API Key"]='(?i)(inforu|informobile)[_\s-]*(api|key|token)[_\s]*[=:]\s*["\x27]?[a-zA-Z0-9]{16,}["\x27]?'
PATTERNS["019 SMS API Key"]='(?i)019[_\s-]*(sms|api|key|token)[_\s]*[=:]\s*["\x27]?[a-zA-Z0-9]{16,}["\x27]?'

# Supabase
PATTERNS["Supabase Service Role Key"]='(?i)(supabase|service[_\s-]*role)[_\s-]*(key|secret)[_\s]*[=:]\s*["\x27]?eyJ[a-zA-Z0-9_-]{20,}["\x27]?'
PATTERNS["Supabase Anon Key (in backend)"]='(?i)supabase[_\s-]*anon[_\s-]*(key)[_\s]*[=:]\s*["\x27]?eyJ[a-zA-Z0-9_-]{20,}["\x27]?'

# Israeli Bank APIs
PATTERNS["Israeli Bank API Credential"]='(?i)(poalim|leumi|discount|mizrahi|hapoalim)[_\s-]*(api|key|token|secret|password)[_\s]*[=:]\s*["\x27]?[a-zA-Z0-9]{10,}["\x27]?'

# Government APIs
PATTERNS["Gov.il API Token"]='(?i)(gov\.il|government|misrad)[_\s-]*(api|key|token)[_\s]*[=:]\s*["\x27]?[a-zA-Z0-9]{16,}["\x27]?'

# Israel Post
PATTERNS["Israel Post API Key"]='(?i)(israel[_\s-]*post|doar[_\s-]*israel)[_\s-]*(api|key|token)[_\s]*[=:]\s*["\x27]?[a-zA-Z0-9]{10,}["\x27]?'

# Generic sensitive patterns
PATTERNS["Hardcoded Password"]='(?i)(password|passwd|pwd)[_\s]*[=:]\s*["\x27][^\x27"]{3,}["\x27]'
PATTERNS["Private Key File"]='-----BEGIN (RSA |EC |DSA |OPENSSH )?PRIVATE KEY-----'
PATTERNS["JWT Token (hardcoded)"]='eyJ[a-zA-Z0-9_-]{10,}\.eyJ[a-zA-Z0-9_-]{10,}\.[a-zA-Z0-9_-]{10,}'
PATTERNS["Israeli ID Number"]='(?i)(teudat[_\s-]*zehut|israeli?[_\s-]*id|tz[_\s-]*number)[_\s]*[=:]\s*["\x27]?\d{9}["\x27]?'

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

    # Use grep with Perl regex
    local results
    results=$(grep -rnP "$pattern" "$PROJECT_DIR" $EXCLUDE_ARGS 2>/dev/null || true)

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
        if [[ "$env_file" == *".env.example"* ]]; then
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
scan_pattern "Cardcom Terminal Number" "${PATTERNS["Cardcom Terminal Number"]}" "CRITICAL"
scan_pattern "Tranzila Supplier Code" "${PATTERNS["Tranzila Supplier Code"]}" "CRITICAL"
scan_pattern "PayMe Seller ID" "${PATTERNS["PayMe Seller ID"]}" "CRITICAL"
scan_pattern "Meshulam API Key" "${PATTERNS["Meshulam API Key"]}" "CRITICAL"
scan_pattern "Cellact API Key" "${PATTERNS["Cellact API Key"]}" "CRITICAL"
scan_pattern "InforUMobile API Key" "${PATTERNS["InforUMobile API Key"]}" "CRITICAL"
scan_pattern "019 SMS API Key" "${PATTERNS["019 SMS API Key"]}" "CRITICAL"
scan_pattern "Supabase Service Role Key" "${PATTERNS["Supabase Service Role Key"]}" "CRITICAL"
scan_pattern "Supabase Anon Key (in backend code)" "${PATTERNS["Supabase Anon Key (in backend)"]}" "HIGH"
scan_pattern "Israeli Bank API Credential" "${PATTERNS["Israeli Bank API Credential"]}" "CRITICAL"
scan_pattern "Gov.il API Token" "${PATTERNS["Gov.il API Token"]}" "HIGH"
scan_pattern "Israel Post API Key" "${PATTERNS["Israel Post API Key"]}" "HIGH"
scan_pattern "Hardcoded Password" "${PATTERNS["Hardcoded Password"]}" "HIGH"
scan_pattern "Private Key File" "${PATTERNS["Private Key File"]}" "CRITICAL"
scan_pattern "JWT Token (hardcoded)" "${PATTERNS["JWT Token (hardcoded)"]}" "HIGH"
scan_pattern "Israeli ID Number" "${PATTERNS["Israeli ID Number"]}" "HIGH"

# Additional checks
check_env_files
check_git_history

print_summary

# Exit with non-zero if critical findings
if [ "$CRITICAL_FINDINGS" -gt 0 ]; then
    exit 1
fi
