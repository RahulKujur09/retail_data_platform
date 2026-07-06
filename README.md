# Retail Data Platform

![Python](https://img.shields.io/badge/Python-3.12-blue)
![DuckDB](https://img.shields.io/badge/DuckDB-Lakehouse-yellow)
![dbt](https://img.shields.io/badge/dbt-Analytics-orange)
![Parquet](https://img.shields.io/badge/Storage-Parquet-green)

---

# Project Overview

This project implements an end-to-end Retail Data Platform using Medallion Architecture.

Raw CSV files are ingested into Bronze Parquet files, transformed into Silver Parquet datasets, queried using DuckDB, modeled with dbt into a Star Schema, and finally exposed through Business Gold analytical models.

---

# Architecture

```
CSV

↓

Bronze (Parquet)

↓

Silver (Parquet)

↓

DuckDB Compute Layer

↓

dbt Staging

↓

dbt Star Schema

↓

Business Gold

↓

Dashboard / BI
```

---

# Tech Stack

| Component | Technology |
|-----------------|----------------|
| Language | Python |
| Storage | Parquet |
| Compute | DuckDB |
| Transformation | dbt |
| Modeling | Star Schema |
| Incremental | dbt Incremental |
| SCD Type 2 | dbt Snapshots |

---

# Medallion Architecture

## Bronze

Raw immutable data stored as Parquet.

## Silver

Cleaned and standardized Parquet datasets.

## DuckDB

Acts as the compute layer querying Parquet directly.

## dbt Staging

Standardized business-ready staging models.

## dbt Marts

Star schema implementation.

Dimensions

- dim_customers
- dim_products
- dim_sellers
- dim_geography
- dim_date

Fact

- fact_sales

## Business Gold

Business-ready analytical models.

- sales_summary_daily
- sales_summary_monthly
- seller_performance
- customer_lifetime_value
- top_products

---

# Features

✅ Medallion Architecture

✅ Star Schema

✅ Incremental Fact Loading

✅ Slowly Changing Dimension Type 2

✅ dbt Tests

✅ Business Gold Layer

✅ Parquet Lakehouse Storage

---

# Project Structure

```
retail-data-platform/

bronze/

silver/

dbt/

models/

staging/

marts/

business/

snapshots/

tests/

docs/

README.md
```

---

# Future Improvements

Power BI Dashboard

Airflow Orchestration

Docker

CI/CD

Great Expectations

Cloud Deployment

## Production readiness additions

- CI workflow added under [.github/workflows/ci.yml](.github/workflows/ci.yml)
- CD workflow added under [.github/workflows/cd.yml](.github/workflows/cd.yml)
- Example environment variables are available in [.env.example](.env.example)
- Health checks are available via [healthcheck.py](healthcheck.py)
- Container images now include health checks in [Dockerfile](Dockerfile) and [airflow/Dockerfile](airflow/Dockerfile)
- Retry handling was added in [src/common/retry.py](src/common/retry.py) for orchestration steps
- Deployment helper script is available at [scripts/deploy.sh](scripts/deploy.sh)