from pyspark.sql import DataFrame
from src.models.config_models import DatasetConfig


def write_data(
    df: DataFrame,
    config: DatasetConfig
):

    destination = config.destination

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