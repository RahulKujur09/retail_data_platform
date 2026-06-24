from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT/"data"

LANDING = DATA_DIR/"landing"
BRONZE = DATA_DIR/"bronze"
SILVER = DATA_DIR/"silver"
GOLD = DATA_DIR/"gold"