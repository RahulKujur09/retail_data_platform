import importlib

from src.common.paths import PROJECT_ROOT
from src.common.reader import read_data
from src.common.writer import write_data
from src.common.silver_config_loader import load_dataset_config

from src.validation.quality import validate_dataframe


def transform_to_silver(
    spark,
    dataset_name: str
):

    config = load_dataset_config(dataset_name)
    
    config["source"]["path"] = str(
    PROJECT_ROOT / config["source"]["path"]
        )

    config["destination"]["path"] = str(
    PROJECT_ROOT / config["destination"]["path"]
        )

    transformation = config["transformation"]

    quality = config.get("quality", {})

    required_columns = quality.get(
        "required_columns",
        []
    )

    key_columns = quality.get(
        "key_columns",
        []
    )

    df = read_data(
        spark=spark,
        config=config
    )

    validate_dataframe(
        df=df,
        required_columns=required_columns,
        key_columns=key_columns
    )

    records_read = df.count()

    module = importlib.import_module(
        transformation["module"]
    )

    transformation_function = getattr(
        module,
        transformation["function"]
    )

    df = transformation_function(df)

    validate_dataframe(
        df=df,
        required_columns=required_columns,
        key_columns=key_columns
    )

    records_written = df.count()

    write_data(
        df=df,
        config=config
    )

    return records_read, records_written