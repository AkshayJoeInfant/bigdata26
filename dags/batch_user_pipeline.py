from airflow import DAG
from airflow.providers.google.cloud.operators.dataproc import DataprocSubmitPySparkJobOperator
from datetime import datetime

with DAG('user_batch_update', start_date=datetime(2024, 1, 1), schedule_interval='@daily') as dag:
    
    # This proves you can orchestrate Spark jobs for Batch ETL
    submit_pyspark = DataprocSubmitPySparkJobOperator(
        task_id='run_spark_scd2',
        main='gs://your-bucket/scripts/batch_user_scd2.py',
        cluster_name='data-cluster-01',
        region='us-central1'
    )