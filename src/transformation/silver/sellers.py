from pyspark.sql.dataframe import DataFrame
from pyspark.sql.functions import trim, upper, lower, col

def transform(df : DataFrame) -> DataFrame:
    df = df.withColumn(
    "seller_id",
    trim("seller_id")
    ).withColumn(
        "seller_city",
        lower(trim(col("seller_city")))
        ).withColumn(
            "seller_state",
            upper(trim(col("seller_state")))
            )
    
    return df