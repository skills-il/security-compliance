#!/usr/bin/env python3
"""
Israeli AppSec Audit Checklist
Automated security audit script that checks common vulnerabilities
in Israeli web applications.

Usage:
    python security-audit-checklist.py --project-dir /path/to/project
    python security-audit-checklist.py --project-dir /path/to/project --format json
    python security-audit-checklist.py --project-dir /path/to/project --check secrets
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Any


# ---------------------------------------------------------------------------
# Bidirectional control characters (Trojan Source detection)
# ---------------------------------------------------------------------------
BIDI_CHARS = re.compile(
    "[\u202a\u202b\u202c\u202d\u202e\u2066\u2067\u2068\u2069]"
)

# ---------------------------------------------------------------------------
# Patterns for Israeli service credentials
# ---------------------------------------------------------------------------
ISRAELI_SECRET_PATTERNS = {
    "cardcom_terminal": re.compile(
        r"(?i)(cardcom|terminal)[\s]*[=:]\s*[\"']?\d{6,8}[\"']?"
    ),
    "tranzila_supplier": re.compile(
        r"(?i)(tranzila|supplier)[\s]*[=:]\s*[\"']?[a-zA-Z0-9]{4,20}[\"']?"
    ),
    "israeli_sms_api_key": re.compile(
        r"(?i)(cellact|inforu|019sms)[\s_-]*(api|key|token)[\s]*[=:]\s*[\"']?[a-zA-Z0-9]{16,}[\"']?"
    ),
    "supabase_service_role": re.compile(
        r"(?i)(supabase|service.?role)[\s_-]*(key|secret)[\s]*[=:]\s*[\"']?eyJ[a-zA-Z0-9_-]{20,}[\"']?"
    ),
    "generic_api_key": re.compile(
        r"(?i)(api[_-]?key|api[_-]?secret|access[_-]?token)[\s]*[=:]\s*[\"']?[a-zA-Z0-9]{20,}[\"']?"
    ),
    "israeli_id_number": re.compile(
        r"(?i)(teudat.?zehut|israeli?.?id|tz.?number)[\s]*[=:]\s*[\"']?\d{9}[\"']?"
    ),
}

# ---------------------------------------------------------------------------
# Insecure patterns in code
# ---------------------------------------------------------------------------
INSECURE_CODE_PATTERNS = {
    "sql_string_concat": re.compile(
        r"""(?i)(SELECT|INSERT|UPDATE|DELETE)\s+.*\+\s*['"]?\s*\w+"""
    ),
    "eval_usage": re.compile(r"\beval\s*\("),
    "innerhtml_usage": re.compile(r"\.innerHTML\s*="),
    "dangerously_set_html": re.compile(r"dangerouslySetInnerHTML"),
    "http_no_tls": re.compile(r"""['"]http://(?!localhost|127\.0\.0\.1)"""),
    "hardcoded_password": re.compile(
        r"""(?i)(password|passwd|pwd)[\s]*[=:]\s*['"][^'"]{3,}['"]"""
    ),
    "md5_usage": re.compile(r"(?i)(md5|sha1)\s*\("),
    "cors_wildcard": re.compile(
        r"""(?i)(access-control-allow-origin|cors).*['"]\*['"]"""
    ),
}

# ---------------------------------------------------------------------------
# Security header checks
# ---------------------------------------------------------------------------
RECOMMENDED_HEADERS = [
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Strict-Transport-Security",
    "Referrer-Policy",
    "Permissions-Policy",
]

# ---------------------------------------------------------------------------
# File extensions to scan
# ---------------------------------------------------------------------------
SCAN_EXTENSIONS = {
    ".ts", ".tsx", ".js", ".jsx", ".py", ".java", ".go",
    ".rb", ".php", ".env", ".yaml", ".yml", ".json", ".toml",
    ".cfg", ".conf", ".ini", ".sh", ".bash",
}

SKIP_DIRS = {
    "node_modules", ".git", ".next", "dist", "build", "__pycache__",
    ".venv", "venv", ".cache", "coverage", ".turbo",
}


def find_project_files(project_dir: str) -> list[Path]:
    """Collect scannable files, skipping vendored and build directories."""
    files: list[Path] = []
    root = Path(project_dir)
    for path in root.rglob("*"):
        if any(skip in path.parts for skip in SKIP_DIRS):
            continue
        if path.is_file() and path.suffix in SCAN_EXTENSIONS:
            files.append(path)
    return files


# ---------------------------------------------------------------------------
# Check: Bidirectional control characters (Trojan Source)
# ---------------------------------------------------------------------------
def check_bidi_chars(files: list[Path]) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    for fp in files:
        try:
            content = fp.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        for line_num, line in enumerate(content.splitlines(), 1):
            matches = BIDI_CHARS.findall(line)
            if matches:
                findings.append({
                    "check": "trojan_source",
                    "severity": "HIGH",
                    "file": str(fp),
                    "line": line_num,
                    "message": (
                        f"Found {len(matches)} bidirectional control "
                        f"character(s) (potential Trojan Source attack)"
                    ),
                })
    return findings


# ---------------------------------------------------------------------------
# Check: Israeli service credential leaks
# ---------------------------------------------------------------------------
def check_secrets(files: list[Path]) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    for fp in files:
        try:
            content = fp.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        for line_num, line in enumerate(content.splitlines(), 1):
            for name, pattern in ISRAELI_SECRET_PATTERNS.items():
                if pattern.search(line):
                    findings.append({
                        "check": "secrets",
                        "severity": "CRITICAL",
                        "file": str(fp),
                        "line": line_num,
                        "message": (
                            f"Potential {name.replace('_', ' ')} "
                            f"detected in source"
                        ),
                    })
    return findings


# ---------------------------------------------------------------------------
# Check: Insecure code patterns
# ---------------------------------------------------------------------------
def check_insecure_code(files: list[Path]) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    for fp in files:
        if fp.suffix in {".env", ".yaml", ".yml", ".json", ".toml", ".cfg",
                         ".conf", ".ini"}:
            continue
        try:
            content = fp.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        for line_num, line in enumerate(content.splitlines(), 1):
            for name, pattern in INSECURE_CODE_PATTERNS.items():
                if pattern.search(line):
                    severity = "HIGH" if name in (
                        "sql_string_concat", "eval_usage"
                    ) else "MEDIUM"
                    findings.append({
                        "check": "insecure_code",
                        "severity": severity,
                        "file": str(fp),
                        "line": line_num,
                        "message": (
                            f"Insecure pattern: {name.replace('_', ' ')}"
                        ),
                    })
    return findings


# ---------------------------------------------------------------------------
# Check: Missing .gitignore entries for sensitive files
# ---------------------------------------------------------------------------
def check_gitignore(project_dir: str) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    gitignore_path = Path(project_dir) / ".gitignore"

    sensitive_patterns = [
        ".env", ".env.local", ".env.production",
        "*.pem", "*.key", "serviceAccountKey.json",
    ]

    if not gitignore_path.exists():
        findings.append({
            "check": "gitignore",
            "severity": "HIGH",
            "file": str(gitignore_path),
            "line": 0,
            "message": "No .gitignore file found in project root",
        })
        return findings

    content = gitignore_path.read_text(encoding="utf-8", errors="ignore")
    for pattern in sensitive_patterns:
        if pattern not in content:
            findings.append({
                "check": "gitignore",
                "severity": "MEDIUM",
                "file": str(gitignore_path),
                "line": 0,
                "message": (
                    f"Sensitive pattern '{pattern}' not found in .gitignore"
                ),
            })
    return findings


# ---------------------------------------------------------------------------
# Check: Exposed .env files
# ---------------------------------------------------------------------------
def check_env_files(project_dir: str) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    root = Path(project_dir)
    for env_file in root.rglob(".env*"):
        if any(skip in env_file.parts for skip in SKIP_DIRS):
            continue
        if env_file.name == ".env.example":
            continue
        if env_file.is_file():
            findings.append({
                "check": "env_files",
                "severity": "HIGH",
                "file": str(env_file),
                "line": 0,
                "message": (
                    f"Environment file '{env_file.name}' found. "
                    f"Ensure it is not committed to version control."
                ),
            })
    return findings


# ---------------------------------------------------------------------------
# Check: Package.json security (dependency lock, scripts)
# ---------------------------------------------------------------------------
def check_package_security(project_dir: str) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    root = Path(project_dir)

    for pkg_json in root.rglob("package.json"):
        if any(skip in pkg_json.parts for skip in SKIP_DIRS):
            continue
        try:
            data = json.loads(
                pkg_json.read_text(encoding="utf-8", errors="ignore")
            )
        except (json.JSONDecodeError, Exception):
            continue

        scripts = data.get("scripts", {})
        for script_name, script_cmd in scripts.items():
            if "curl" in script_cmd or "wget" in script_cmd:
                findings.append({
                    "check": "package_security",
                    "severity": "MEDIUM",
                    "file": str(pkg_json),
                    "line": 0,
                    "message": (
                        f"Script '{script_name}' downloads from external "
                        f"source. Verify the URL is trusted."
                    ),
                })

    lock_files = ["pnpm-lock.yaml", "package-lock.json", "yarn.lock"]
    has_lock = any((root / lf).exists() for lf in lock_files)
    if not has_lock:
        findings.append({
            "check": "package_security",
            "severity": "MEDIUM",
            "file": str(root),
            "line": 0,
            "message": "No package lockfile found. Dependency integrity cannot be verified.",
        })

    return findings


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------
def generate_report(
    findings: list[dict[str, Any]], fmt: str = "text"
) -> str:
    if fmt == "json":
        summary = {
            "total_findings": len(findings),
            "by_severity": {},
            "by_check": {},
            "findings": findings,
        }
        for f in findings:
            sev = f["severity"]
            chk = f["check"]
            summary["by_severity"][sev] = summary["by_severity"].get(sev, 0) + 1
            summary["by_check"][chk] = summary["by_check"].get(chk, 0) + 1
        return json.dumps(summary, indent=2, ensure_ascii=False)

    # Plain text report
    lines: list[str] = []
    lines.append("=" * 60)
    lines.append("  Israeli AppSec Audit Report")
    lines.append("=" * 60)
    lines.append("")

    severity_order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}
    sorted_findings = sorted(
        findings, key=lambda f: severity_order.get(f["severity"], 99)
    )

    counts: dict[str, int] = {}
    for f in sorted_findings:
        counts[f["severity"]] = counts.get(f["severity"], 0) + 1

    lines.append("Summary:")
    for sev in ["CRITICAL", "HIGH", "MEDIUM", "LOW"]:
        if sev in counts:
            lines.append(f"  [{sev}] {counts[sev]} finding(s)")
    lines.append(f"  Total: {len(findings)} finding(s)")
    lines.append("")
    lines.append("-" * 60)

    for f in sorted_findings:
        lines.append(
            f"[{f['severity']}] {f['check']}: {f['message']}"
        )
        if f["line"] > 0:
            lines.append(f"  File: {f['file']}:{f['line']}")
        else:
            lines.append(f"  File: {f['file']}")
        lines.append("")

    if not findings:
        lines.append("No findings detected. Review manually for completeness.")
        lines.append("")

    lines.append("=" * 60)
    lines.append("  Scan complete. Review findings and remediate by severity.")
    lines.append("=" * 60)
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> None:
    parser = argparse.ArgumentParser(
        description="Israeli AppSec Audit Checklist"
    )
    parser.add_argument(
        "--project-dir",
        required=True,
        help="Path to the project directory to scan",
    )
    parser.add_argument(
        "--format",
        choices=["text", "json"],
        default="text",
        help="Output format (default: text)",
    )
    parser.add_argument(
        "--check",
        choices=[
            "all", "secrets", "bidi", "insecure_code",
            "gitignore", "env_files", "packages",
        ],
        default="all",
        help="Which check to run (default: all)",
    )
    args = parser.parse_args()

    project_dir = os.path.abspath(args.project_dir)
    if not os.path.isdir(project_dir):
        print(f"Error: '{project_dir}' is not a valid directory.", file=sys.stderr)
        sys.exit(1)

    files = find_project_files(project_dir)
    print(f"Scanning {len(files)} files in {project_dir}...", file=sys.stderr)

    findings: list[dict[str, Any]] = []

    checks = args.check
    if checks in ("all", "bidi"):
        findings.extend(check_bidi_chars(files))
    if checks in ("all", "secrets"):
        findings.extend(check_secrets(files))
    if checks in ("all", "insecure_code"):
        findings.extend(check_insecure_code(files))
    if checks in ("all", "gitignore"):
        findings.extend(check_gitignore(project_dir))
    if checks in ("all", "env_files"):
        findings.extend(check_env_files(project_dir))
    if checks in ("all", "packages"):
        findings.extend(check_package_security(project_dir))

    report = generate_report(findings, fmt=args.format)
    print(report)

    # Exit with non-zero if critical or high findings
    critical_high = [
        f for f in findings if f["severity"] in ("CRITICAL", "HIGH")
    ]
    if critical_high:
        sys.exit(1)


if __name__ == "__main__":
    main()
