from pyspark.sql.dataframe import DataFrame
from pyspark.sql.functions import coalesce, lit, col
from src.common import constants

def transform(df : DataFrame) -> DataFrame:
    df = (
    df
    .withColumn("product_category_name", 
                coalesce(col("product_category_name"), lit(constants.STRING_DEFAULT)))
    .withColumn("product_name_lenght", 
                coalesce(col("product_name_lenght"), lit(constants.INT_DEFAULT)))
    .withColumn("product_description_lenght", 
                coalesce(col("product_description_lenght"), lit(constants.INT_DEFAULT)))
    .withColumn("product_photos_qty", 
                coalesce(col("product_photos_qty"), lit(constants.INT_DEFAULT)))
    .withColumn("product_weight_g", 
                coalesce(col("product_weight_g"), lit(constants.INT_DEFAULT)))
    .withColumn("product_length_cm", 
                coalesce(col("product_length_cm"), lit(constants.INT_DEFAULT)))
    .withColumn("product_height_cm", 
                coalesce(col("product_height_cm"), lit(constants.INT_DEFAULT)))
    .withColumn("product_width_cm", 
                coalesce(col("product_width_cm"), lit(constants.INT_DEFAULT)))
                )

    return df