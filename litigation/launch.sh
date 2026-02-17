#!/usr/bin/env bash
# Launch courtroom litigation runner.
# Run from project root: ./litigation/launch.sh [matter]
# Or: ./litigation/launch.sh  (interactive mode)
#
# Activates litigation/.venv, installs requirements, loads .env from litigation/providers/.env

set -e
cd "$(dirname "$0")/.."
LITIGATION_DIR="$(cd litigation && pwd)"
VENV="${LITIGATION_DIR}/.venv"

# Create venv if not exists
if [[ ! -d "${VENV}" ]]; then
  python3 -m venv "${VENV}"
fi

# Activate venv
source "${VENV}/bin/activate"

# Install requirements
pip install -q -r "${LITIGATION_DIR}/requirements.txt"

# Run (loads dotenv from litigation/providers/.env automatically)
exec python "${LITIGATION_DIR}/run.py" "$@"
