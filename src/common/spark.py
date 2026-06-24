from pyspark.sql.session import SparkSession

from src.common.config import load_yaml
from src.common.logger import logger
from src.common.paths import PROJECT_ROOT

APP_CONFIG = load_yaml(PROJECT_ROOT / "configs" / "app.yaml")

def create_spark_session():

    logger.info("Creating Spark Session")

    spark = (
        SparkSession.builder
        .appName(APP_CONFIG["spark"]["app_name"])
        .master(APP_CONFIG["spark"]["master"])
        .getOrCreate()
    )

    logger.info("Spark Session Created")

    return spark