from prefect import flow, get_run_logger

@flow
def hello():
    get_run_logger().info("Howdy!")
