from typing import Any

from pyspark.sql import DataFrame

from src.models.config_models import DatasetConfig


def _coerce_config(config: DatasetConfig | dict[str, Any]) -> DatasetConfig:
    if isinstance(config, DatasetConfig):
        return config
    if isinstance(config, dict):
        return DatasetConfig(**config)
    raise TypeError("config must be a DatasetConfig or dict")


def write_data(
    df: DataFrame,
    config: DatasetConfig | dict[str, Any]
):

    config_model = _coerce_config(config)
    destination = config_model.destination

    if destination.format == "parquet":

        (
            df.write
            .mode(destination.mode)
            .parquet(destination.path)
        )

    elif destination.format == "csv":

        (
            df.write
            .mode(destination.mode)
            .option("header", True)
            .csv(destination.path)
        )

    else:

        raise ValueError(
            f"Unsupported output format: {destination.format}"
        )