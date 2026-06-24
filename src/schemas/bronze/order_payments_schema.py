from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    IntegerType,
    FloatType
)

ORDER_PAYMENTS_DATASET_SCHEMA = StructType(
    [
        (StructField("order_id", StringType(), True)),
        (StructField("payment_sequential", IntegerType(), True)),
        (StructField("payment_type", StringType(), True)),
        (StructField("payment_installments", IntegerType(), True)),
        (StructField("payment_value", FloatType(), True))
    ]
)