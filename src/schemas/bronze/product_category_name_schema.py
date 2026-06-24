from pyspark.sql.types import (
    StructType,
    StructField,
    StringType
)

PRODUCT_CATEGORY_NAME_SCHEMA = StructType(
    [
        (StructField("product_category_name", StringType(), True)),
        (StructField("product_category_name_english", StringType(), True))
    ]
)