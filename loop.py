from prefect import flow, get_run_logger
import time

@flow
def loop():
    logger = get_run_logger()
    n = 0

    while True:
        logger.info(n)
        n += 1
        time.sleep(2)