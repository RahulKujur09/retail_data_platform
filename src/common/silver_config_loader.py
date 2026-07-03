from pathlib import Path
import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def load_dataset_config(dataset_name):

    config_path = (
        PROJECT_ROOT
        / "configs"
        / "silver"
        / f"{dataset_name}.yaml"
    )

    with open(config_path, "r") as file:
        return yaml.safe_load(file)