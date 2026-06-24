from pyspark.sql.functions import (
    current_timestamp,
    current_date,
    input_file_name,
    lit
)


def add_metadata(df, dataset_name):

    return (
        df
        .withColumn("_ingestion_timestamp", current_timestamp())
        .withColumn("_load_date", current_date())
        .withColumn("_source_file", input_file_name())
        .withColumn("_dataset_name", lit(dataset_name))
        .withColumn("_pipeline_version", lit("1.0"))
    )