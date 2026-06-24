from pyspark.sql import DataFrame


def write_data(df: DataFrame, config: dict):

    destination = config["destination"]

    output_format = destination["format"]

    mode = destination.get("mode", "overwrite")

    path = destination["path"]

    if output_format == "parquet":

        (
            df.write
            .mode(mode)
            .parquet(path)
        )

    elif output_format == "csv":

        (
            df.write
            .mode(mode)
            .option("header", True)
            .csv(path)
        )

    else:

        raise ValueError(f"Unsupported output format : {output_format}")