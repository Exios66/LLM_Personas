#!/usr/bin/env bash
#
# MORNINGSTAR Court Reporter — Cron Launcher
#
# Run every 3 hours to sync courtroom documentation.
# Add to crontab: 0 */3 * * * /path/to/LLM_Personas/scripts/run-court-reporter.sh
#
# Usage:
#   ./scripts/run-court-reporter.sh
#   ./scripts/run-court-reporter.sh >> /tmp/court-reporter.log 2>&1  # with logging
#

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$REPO_ROOT"

python3 courtroom/reporter.py
