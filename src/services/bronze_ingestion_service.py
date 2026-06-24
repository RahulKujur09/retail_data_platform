import importlib

from src.common.bronze_config_loader import load_dataset_config
from src.common.reader import read_data
from src.common.writer import write_data

from src.services.enrichment import add_metadata

from src.validation.quality import validate_dataframe


def ingest_to_bronze(
    spark,
    dataset_name: str
):

    config = load_dataset_config(dataset_name)

    schema_module = config["schema"]["module"]
    schema_variable = config["schema"]["variable"]

    module = importlib.import_module(schema_module)

    schema = getattr(module, schema_variable)

    df = read_data(
        spark=spark,
        config=config,
        schema=schema
    )

    quality = config.get("quality", {})

    required_columns = quality.get("required_columns", [])

    key_columns = quality.get(
        "key_columns",
        []
    )

    validate_dataframe(
        df = df,
        required_columns = required_columns,
        key_columns= key_columns
    )

    df = add_metadata(
        df=df,
        dataset_name=dataset_name
    )

    write_data(
        df=df,
        config=config
    )

    print(f"{dataset_name} bronze ingestion completed.")