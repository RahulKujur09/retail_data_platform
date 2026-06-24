from pyspark.sql.functions import trim, col
from pyspark.sql.dataframe import DataFrame

def transform(df : DataFrame) -> DataFrame:
    df = (
    df
    .withColumn("product_category_name", trim(col("product_category_name")))
    .withColumn("product_category_name_english", trim(col("product_category_name_english")))
    )
    
    return df