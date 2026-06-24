from pyspark.sql.functions import upper, lower, trim, col
from pyspark.sql.dataframe import DataFrame

def transform(df : DataFrame) -> DataFrame:
    df = df.withColumn(
        "geolocation_city",
        lower(trim(col("geolocation_city"))
              )
            ).withColumn(
                "geolocation_state",
                upper(trim(col("geolocation_state")))
                )
    
    return df