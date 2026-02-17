#!/usr/bin/env bash
# Launch courtroom litigation runner.
# Run from project root: ./litigation/launch.sh [matter]
# Or: ./litigation/launch.sh  (interactive mode)

set -e
cd "$(dirname "$0")/.."
exec python3 litigation/run.py "$@"
