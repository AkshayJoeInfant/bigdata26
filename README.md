Fact Table: fact_sales (Grain: One row per transaction).

Dimension Table: dim_users (SCD Type 2 to track history).

Dimension Table: dim_products (Standard lookup).

# End-to-End Big Data Pipeline: E-Commerce Analytics (Medallion Architecture)

## 🚀 Project Overview
This project demonstrates a production-grade **Lambda Architecture** on GCP. It handles both high-velocity streaming order data and daily batch user updates, implementing advanced data modeling and quality validation.

### Key Features:
- **Streaming Ingestion**: Real-time orders via Pub/Sub and Dataflow.
- **Batch Processing**: Daily user updates processed via Dataproc (PySpark).
- **Data Modeling**: Star Schema with **SCD Type 2** tracking in BigQuery.
- **Data Quality**: Automated validation using **dbt (data build tool)**.
- **Orchestration**: Managed workflow via **Apache Airflow (Cloud Composer)**.

## 🏗️ Architecture


## 📊 Data Modeling (The "Gold" Layer)
- **Fact Table**: `fact_sales` (Partitioned by Date)
- **Dimension Table**: `dim_users` (SCD Type 2 to track historical address changes)
- **Dimension Table**: `dim_products`