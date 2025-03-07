from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime

default_args = {
    'owner': 'tenant1',
    'start_date': datetime(2023, 10, 1),
}

with DAG('tenant1_dag', default_args=default_args, schedule_interval='@daily') as dag:
    task1 = DummyOperator(task_id='task1')
    task2 = DummyOperator(task_id='task2')
    task1 >> task2