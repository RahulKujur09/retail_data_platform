import subprocess


def main():
    subprocess.run(
        ["dbt", "run"],
        cwd="/opt/airflow/retail_data_platform/dbt",
        check=True,
    )

    subprocess.run(
        ["dbt", "snapshot"],
        cwd="/opt/airflow/retail_data_platform/dbt",
        check=True,
    )


if __name__ == "__main__":
    main()