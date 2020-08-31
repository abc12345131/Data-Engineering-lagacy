from datetime import timedelta
import airflow
from airflow import DAG
from airflow.contrib.operators.emr_create_job_flow_operator import EmrCreateJobFlowOperator
from airflow.contrib.operators.emr_add_steps_operator import EmrAddStepsOperator
from airflow.contrib.sensors.emr_step_sensor import EmrStepSensor
from airflow.contrib.operators.emr_terminate_job_flow_operator import EmrTerminateJobFlowOperator
from airflow.operators.python_operator import PythonOperator


DEFAULT_ARGS = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(0),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False
}


CLUSTER_ID = 'your-cluster'

SPARK_TEST_STEPS = [
    {
        'Name': 'datajob',
        'ActionOnFailure': 'CONTINUE',
        'HadoopJarStep': {
            'Jar': 'command-runner.jar',
            'Args': [
                '/usr/bin/spark-submit',
                '--class', 'Driver.MainApp',
                '--master', 'yarn',
                '--deploy-mode','cluster',
                '--num-executors','2',
                '--driver-memory','512m',
                '--executor-memory','3g',
                '--executor-cores','2',
                'your-jar',
                '-p','wcd-demo',
                '-i','Csv',
                '-o','parquet',
                '-s','your-input',
                #'-s', "{{ task_instance.xcom_pull('parse_request', key='s3location') }}",
                '-d','your-result',
                '-c','job',
                '-m','append',
                '--input-options','header=true'
            ]
        }
    }
]


dag = DAG(
    dag_id='emr_job_flow_manual_steps_dag',
    default_args=DEFAULT_ARGS,
    dagrun_timeout=timedelta(hours=2),
    schedule_interval=None
)


step_adder = EmrAddStepsOperator(
    task_id='add_steps',
    job_flow_id=CLUSTER_ID,
    aws_conn_id='aws_default',
    steps=SPARK_TEST_STEPS,
    dag=dag
)

step_checker = EmrStepSensor(
    task_id='watch_step',
    job_flow_id=CLUSTER_ID,
    step_id="{{ task_instance.xcom_pull('add_steps', key='return_value')[0] }}",
    aws_conn_id='aws_default',
    dag=dag
)


step_checker.set_upstream(step_adder)
