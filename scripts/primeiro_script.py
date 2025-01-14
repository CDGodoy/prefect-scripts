import pandas as pd

from prefect import flow, task

@flow(log_prints=True)
def show_ola():
    print("ola")
    show_mundo()

@task
def show_mundo():
    print("mundo")

if __name__ == "__main__":
    show_ola()