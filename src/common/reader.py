from pyspark.sql import DataFrame
from src.models.config_models import DatasetConfig


def read_data(
    spark,
    config: DatasetConfig,
    schema=None
) -> DataFrame:

    source = config.source

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