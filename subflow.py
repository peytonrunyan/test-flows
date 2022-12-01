from prefect import flow, task, get_run_logger
import time

@task
def first_task():
    get_run_logger().info("First task")

@flow
def loop():
    logger = get_run_logger()
    n = 0

    while True:
        logger.info(n)
        n += 1
        time.sleep(2)

@flow
def run_subflow():
    task()
    loop()