from pyspark.sql.functions import trim, coalesce, lit, col
from pyspark.sql.dataframe import DataFrame
from src.common import constants

def transform(df : DataFrame) -> DataFrame:
    df = df.withColumn(
        "order_id", trim(col("order_id"))
    ).withColumn(
        "payment_sequential",
        coalesce(col("payment_sequential"), lit(constants.INT_DEFAULT))
    ).withColumn(
        "payment_type",
        trim(col("payment_type"))
    )

    return df