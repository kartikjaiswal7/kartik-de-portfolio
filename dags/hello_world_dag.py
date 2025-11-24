from __future__ import annotations
import pendulum
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="hello_world_dag",
    start_date=pendulum.datetime(2023, 1, 1, tz="UTC"),
    schedule=None,
    catchup=False,
    tags=["example"],
) as dag:
    task1 = BashOperator(task_id="say_hello", bash_command="echo 'Hello from Airflow!'")
    task2 = BashOperator(task_id="show_date", bash_command="date")
    task1 >> task2