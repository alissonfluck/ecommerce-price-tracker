from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'data_engineer',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 1, 
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    'ecommerce_price_tracker',
    default_args=default_args,
    description='Pipeline ETL E-commerce',
    schedule='@daily',
    catchup=False,
    tags=['ecommerce', 'scraping'],
) as dag:

    extract_task = BashOperator(
        task_id='run_web_scraper',
        bash_command='python /opt/airflow/scripts/scraper.py'
    )

    extract_task