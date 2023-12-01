from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from pipelines.reddit_pipeline import reddit_pipeline


file_prefix=file_postfix = datetime.now().strftime("%Y%m%d")

default_args={
    'owner':'Morshed Sarwer',
    'start_date':datetime(2023,1,1)
}
dag=DAG(
    dag_id='reddit_data_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
)

extract=PythonOperator(
    task_id='reddit_extraction',
    python_callable=reddit_pipeline,
    op_kwargs={
        'file_name':f'reddit_{file_prefix}',
        'subreddit':'dataengineering',
        'time_filter':'day',
        'limit':100
    }
)

extract