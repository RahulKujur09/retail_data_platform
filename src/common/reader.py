from typing import Any

from pyspark.sql import DataFrame

from src.models.config_models import DatasetConfig, SourceConfig


def _coerce_config(config: DatasetConfig | dict[str, Any]) -> DatasetConfig:
    if isinstance(config, DatasetConfig):
        return config
    if isinstance(config, dict):
        return DatasetConfig(**config)
    raise TypeError("config must be a DatasetConfig or dict")


def read_data(
    spark,
    config: DatasetConfig | dict[str, Any],
    schema=None
) -> DataFrame:

    config_model = _coerce_config(config)
    source = config_model.source

    if source.format == "csv":

        reader = (
            spark.read
            .option("header", source.header)
            .option("delimiter", source.delimiter)
        )

        if schema:
            reader = reader.schema(schema)

        return reader.csv(source.path)

    elif source.format == "parquet":

        return spark.read.parquet(source.path)

    else:

        raise ValueError(
            f"Unsupported format: {source.format}"
        )