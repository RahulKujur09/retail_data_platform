#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

python -m ensurepip --upgrade || true
python -m pip install --upgrade pip
python -m pip install -r requirements.txt pytest

python -m pytest -q
python healthcheck.py
