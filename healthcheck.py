import sys
from pathlib import Path

required_paths = [
    Path("dbt"),
    Path("dags"),
    Path("src"),
]

missing = [path for path in required_paths if not path.exists()]
if missing:
    print("Missing required paths:", ", ".join(str(path) for path in missing))
    sys.exit(1)

print("healthcheck ok")
