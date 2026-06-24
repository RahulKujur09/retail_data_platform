from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    TimestampType,
    IntegerType,
    FloatType,
)

GEOLOCATION_SCHEMA = StructType(
    [
        (StructField("geolocation_zip_code_prefix", IntegerType(), True)),
        (StructField("geolocation_lat", FloatType(), True)),
        (StructField("geolocation_lng", FloatType(), True)),
        (StructField("geolocation_city", StringType(), True)),
        (StructField("geolocation_state", StringType(), True))
    ]
)