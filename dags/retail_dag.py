from airflow.decorators import dag, task
from airflow.operators.python import PythonOperator
from datetime import datetime
from src.orchestration.duckdb_runner import main as run_duckdb
from src.orchestration.bronze_runner import main as run_bronze
from src.orchestration.silver_runner import main as run_silver
from src.orchestration.dbt_runner import main as run_dbt

@dag(dag_id="retail_dag")
def retail_dag():
    run_bronze_task = PythonOperator(
        task_id="run_bronze_pipeline",
        python_callable=run_bronze
    )

    run_silver_task = PythonOperator(
        task_id="run_silver_pipeline",
        python_callable=run_silver
    )

    run_duckdb_task = PythonOperator(
        task_id="run_duckdb_loader",
        python_callable=run_duckdb
    )

    run_dbt_task = PythonOperator(
        task_id="run_dbt",
        python_callable=run_dbt
    )

    run_bronze_task >> run_silver_task >> run_duckdb_task >> run_dbt_task

# Instantiate the DAG
retail_dag()