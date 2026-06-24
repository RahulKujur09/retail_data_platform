from pyspark.sql.functions import trim, coalesce, lit, to_date, date_format, col
from pyspark.sql.dataframe import DataFrame
from src.common import constants


def transform(df : DataFrame) -> DataFrame:
    df = df.withColumnsRenamed(
    {
        "order_approved_at" : "order_approved_at_timestamp",
        "order_delivered_carrier_date" : "order_delivered_carrier_timestamp",
        "order_delivered_customer_date" : "order_delivered_customer_timestamp",
        "order_estimated_delivery_date" : "order_estimated_delivery_timestamp"
            }
        )

    df = (
        df
        .withColumn("order_id", trim(col("order_id")))
        .withColumn("customer_id", trim(col("customer_id")))
        .withColumn("order_status", trim(col("order_status")))
        
        
        .withColumn("order_purchase_timestamp", 
                    coalesce(df["order_purchase_timestamp"], lit(constants.TIMESTAMP_DEFAULT)))
        .withColumn("order_approved_at_timestamp", 
                    coalesce(df["order_approved_at_timestamp"], lit(constants.TIMESTAMP_DEFAULT)))
        .withColumn("order_delivered_carrier_timestamp", 
                    coalesce(df["order_delivered_carrier_timestamp"], lit(constants.TIMESTAMP_DEFAULT)))
        .withColumn("order_delivered_customer_timestamp", 
                    coalesce(df["order_delivered_customer_timestamp"], lit(constants.TIMESTAMP_DEFAULT)))
        .withColumn("order_estimated_delivery_timestamp", 
                    coalesce(df["order_estimated_delivery_timestamp"], lit(constants.TIMESTAMP_DEFAULT)))
        
        .withColumn("order_purchase_date", to_date("order_purchase_timestamp"))
        .withColumn("order_purchase_time", date_format("order_purchase_timestamp", "HH:mm:ss"))
        
        .withColumn("order_approved_at_date", to_date("order_approved_at_timestamp"))
        .withColumn("order_approved_at_time", date_format("order_approved_at_timestamp", "HH:mm:ss"))
        
        .withColumn("order_delivered_carrier_date", to_date("order_delivered_carrier_timestamp"))
        .withColumn("order_delivered_carrier_time", date_format("order_delivered_carrier_timestamp", "HH:mm:ss"))
        
        .withColumn("order_delivered_customer_date", to_date("order_delivered_customer_timestamp"))
        .withColumn("order_delivered_customer_time", date_format("order_delivered_customer_timestamp", "HH:mm:ss"))
        
        .withColumn("order_estimated_delivery_date", to_date("order_estimated_delivery_timestamp"))
        .withColumn("order_estimated_delivery_time", date_format("order_estimated_delivery_timestamp", "HH:mm:ss"))
    )

    return df