from pyspark.sql.dataframe import DataFrame
from pyspark.sql.functions import (
    col,
    upper,
    lower,
    trim
)

def transform(df : DataFrame) -> DataFrame:
    df = df.dropDuplicates(["customer_id"]).withColumn(
            "customer_city",
            lower(trim(col("customer_city"))
                  )
        ).withColumn(
            "customer_state",
            upper(trim(col("customer_state")))
        )
    
    return df