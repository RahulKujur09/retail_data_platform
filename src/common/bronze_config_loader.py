from pathlib import Path
import yaml


def load_dataset_config(dataset_name: str) -> dict:
    """
    Loads dataset configuration yaml.
    """

    config_path = (
        Path("configs")
        / "dataset"
        / f"{dataset_name}.yaml"
    )

    with open(config_path, "r") as file:
        return yaml.safe_load(file)