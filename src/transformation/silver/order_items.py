from pyspark.sql.functions import trim, coalesce, lit, to_date, date_format, col
from pyspark.sql.dataframe import DataFrame
from src.common import constants

def transform(df:DataFrame) -> DataFrame:
    df = df.withColumnsRenamed(
    {
        "shipping_limit_date" : "shipping_limit_timestamp"
    }
    )

    df = df.withColumn(
        "order_id",
        trim(col("order_id"))
    ).withColumn(
        "order_item_id",
        coalesce(col("order_item_id"), lit(constants.INT_DEFAULT))
    ).withColumn(
        "product_id", trim(col("product_id"))
    ).withColumn(
        "seller_id",
        trim(col("seller_id"))
    ).withColumn(
        "shipping_limit_date", to_date("shipping_limit_timestamp")
    ).withColumn(
        "shipping_limit_time",
        date_format("shipping_limit_timestamp", "HH:mm:ss")
    ).withColumn(
        "price",
        coalesce(col("price"), lit(constants.INT_DEFAULT))
    ).withColumn(
        "freight_value",
        coalesce(col("price"), lit(constants.INT_DEFAULT))
    )

    return df