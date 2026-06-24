from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    IntegerType,
    FloatType,
    TimestampType
)

ORDER_ITEMS_SCHEMA = StructType(
    [
        (StructField("order_id", StringType(), True)),
        (StructField("order_item_id", IntegerType(), True)),
        (StructField("product_id", StringType(), True)),
        (StructField("seller_id", StringType(), True)),
        (StructField("shipping_limit_date", TimestampType(), True)),
        (StructField("price", FloatType(), True)),
        (StructField("freight_value", FloatType(), True))
    ]
)