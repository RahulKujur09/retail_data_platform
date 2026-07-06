from src.common.logger import logger
from src.common.retry import run_command_with_retry


def main():
    dbt_dir = "/opt/airflow/retail_data_platform/dbt"
    logger.info("Running dbt models")
    run_command_with_retry(["dbt", "run"], cwd=dbt_dir, description="dbt run")
    logger.info("Running dbt snapshots")
    run_command_with_retry(["dbt", "snapshot"], cwd=dbt_dir, description="dbt snapshot")


if __name__ == "__main__":
    main()