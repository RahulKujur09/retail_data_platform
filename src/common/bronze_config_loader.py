from pathlib import Path
import yaml
from src.models.config_models import DatasetConfig

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def load_dataset_config(dataset_name: str) -> DatasetConfig:

    config_path = (
        PROJECT_ROOT
        / "configs"
        / "dataset"
        / f"{dataset_name}.yaml"
    )

    with open(config_path, "r") as file:
        data =  yaml.safe_load(file)

        return DatasetConfig.model_validate(data)