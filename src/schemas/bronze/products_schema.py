from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    IntegerType,
    FloatType
)

PRODUCT_SCHEMA = StructType(
    [
        (StructField("product_id", StringType(), True)),
        (StructField("product_category_name", StringType(), True)),
        (StructField("product_name_lenght", FloatType(), True)),
        (StructField("product_description_lenght", FloatType(), True)),
        (StructField("product_photos_qty", FloatType(), True)),
        (StructField("product_weight_g", FloatType(), True)),
        (StructField("product_length_cm", FloatType(), True)),
        (StructField("product_height_cm", FloatType(), True)),
        (StructField("product_width_cm", FloatType(), True))
    ]
)