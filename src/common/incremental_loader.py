from pyspark.sql import DataFrame

def get_incremental_records(
    source_df,
    target_df,
    key_columns
):
    if target_df is None:
        return source_df

    if not key_columns:
        # No keys configured -> treat as full load
        return source_df

    return (
        source_df.join(
            target_df.select(*key_columns),
            on=key_columns,
            how="left_anti"
        )
    )