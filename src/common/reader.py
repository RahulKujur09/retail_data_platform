from pyspark.sql import DataFrame


def read_data(spark, config: dict, schema=None) -> DataFrame:

    source = config["source"]

    file_format = source["format"]

    if file_format == "csv":

        reader = (
            spark.read
            .option("header", source.get("header", True))
            .option("delimiter", source.get("delimiter", ","))
        )

        if schema:
            reader = reader.schema(schema)

        return reader.csv(source["path"])

    elif file_format == "parquet":

        return spark.read.parquet(source["path"])

    else:

        raise ValueError(f"Unsupported format : {file_format}")