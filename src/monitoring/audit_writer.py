from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    TimestampType,
    DoubleType,
    LongType,
)

AUDIT_SCHEMA = StructType(
    [
        StructField("run_id", StringType(), False),
        StructField("pipeline_name", StringType(), False),
        StructField("dataset_name", StringType(), False),
        StructField("start_time", TimestampType(), False),
        StructField("end_time", TimestampType(), False),
        StructField("duration_seconds", DoubleType(), False),
        StructField("status", StringType(), False),
        StructField("records_read", LongType(), True),
        StructField("records_written", LongType(), True),
        StructField("error_message", StringType(), True),
    ]
)


def write_audit_log(
    spark: SparkSession,
    audit_record: dict,
):

    df = spark.createDataFrame(
        [audit_record],
        schema=AUDIT_SCHEMA,
    )

    (
        df.write
        .mode("append")
        .parquet("data/audit/pipeline_runs")
    )