from pyspark.sql.functions import trim, coalesce, lit, to_date, date_format, col
from pyspark.sql.dataframe import DataFrame
from src.common import constants

def transform(df : DataFrame) -> DataFrame:
    df = df.withColumnsRenamed(
    {
        "review_creation_date" : "review_creation_timestamp"
    })

    df = df.withColumn(
        "review_id",
        trim(col("review_id"))
    ).withColumn(
        "order_id",
        trim(col("order_id"))
    ).withColumn(
        "review_score",
        coalesce(col("review_score"), lit(constants.INT_DEFAULT))
    ).withColumn(
        "review_comment_title",
        coalesce(col("review_comment_title"), lit(constants.MISSING_REVIEW))
    ).withColumn(
        "review_comment_message",
        coalesce(col("review_comment_message"), lit(constants.MISSING_REVIEW))
    ).withColumn(
        "review_creation_date",
        to_date("review_creation_timestamp")
    ).withColumn(
        "review_creation_time",
        date_format("review_creation_timestamp","HH:mm:ss")
    ).withColumn(
        "review_answer_date",
        to_date("review_answer_timestamp")
    ).withColumn(
        "review_answer_time",
        date_format("review_answer_timestamp","HH:mm:ss")
    )

    return df