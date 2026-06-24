# Retail Data Platform Architecture

## Overview

This project implements a Medallion Architecture using Python, Parquet, DuckDB, and dbt.

The objective is to transform raw e-commerce data into business-ready analytical datasets.

---

## Data Flow

CSV Files
    │
    ▼
Bronze Layer (Parquet)
    │
    ▼
Silver Layer (Parquet)
    │
    ▼
DuckDB Compute Layer
    │
    ▼
dbt Staging Models
    │
    ▼
dbt Star Schema
    │
    ▼
Business Gold Layer
    │
    ▼
Dashboard / BI

---

## Layers

### Bronze

Stores raw source files exactly as received.

Format:
Parquet

Transformation:
None

Purpose:
Immutable raw data storage.

---

### Silver

Stores cleaned and standardized datasets.

Transformations include:

- datatype casting
- duplicate removal
- timestamp conversion
- quality fixes

Format:
Parquet

---

### DuckDB Compute Layer

DuckDB reads Parquet directly without copying data.

This provides:

- fast analytics
- low storage cost
- local data warehouse experience

---

### dbt Staging

Creates standardized views from silver datasets.

Naming:

stg_orders

stg_products

stg_customers

etc.

---

### dbt Marts

Implements dimensional modeling.

Dimensions

dim_customers

dim_products

dim_sellers

dim_geography

dim_date

Fact

fact_sales

---

### Business Gold

Business-ready analytical models.

sales_summary_daily

sales_summary_monthly

customer_lifetime_value

seller_performance

top_products

---

### Advanced Features

Incremental fact loading

SCD Type 2 customer snapshots

dbt tests

Parquet lakehouse storage

Medallion architecture
