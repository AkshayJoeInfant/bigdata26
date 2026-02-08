-- Create the Dataset first
CREATE SCHEMA IF NOT EXISTS `bigdata26.raw_layer`;

-- 1. Table for Streaming Orders (fact_sales source)
-- We use Partitioning by day to handle "Big Data" volumes efficiently.
CREATE OR REPLACE TABLE `bigdata26.raw_layer.orders_stream` (
    order_id STRING,
    user_id STRING,
    product_id STRING,
    amount FLOAT64,
    timestamp TIMESTAMP,
    ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
PARTITION BY DATE(timestamp)
CLUSTER BY user_id;

-- 2. Table for Batch Users (dim_users source for SCD Type 2)
-- We do not partition this yet, as it's a smaller "Master Data" table.
CREATE OR REPLACE TABLE `bigdata26.raw_layer.users_batch` (
    user_id STRING,
    name STRING,
    email STRING,
    address STRING,
    updated_at TIMESTAMP,
    ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);