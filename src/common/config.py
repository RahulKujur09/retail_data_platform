from pathlib import Path
import yaml

def load_yaml(path : str | Path):
    with open(Path(path), "r") as f:
        return yaml.safe_load(f)