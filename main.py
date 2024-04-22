import json
import logging
import multiprocessing
import os
import sys
import time

import numpy as np
from dotenv import load_dotenv

from db_insert import insert_data_into_db
from db_setup import (create_db, create_partition_on_user_action,
                      create_tables, execute_sql_query)
from generate_data import generate_event, generate_users
from patterns import end_date, start_date
from process_data import process_segment
from utility_functions import load_sql_file

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    stream=sys.stdout,
)

load_dotenv()

server = os.getenv("DB_SERVER")
database = os.getenv("DB_DATABASE")
username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
driver = os.getenv("DB_DRIVER")
user_action_days = os.getenv("USER_ACTION_DAYS")
total_users = os.getenv("total_users")
total_events = os.getenv("total_events")
batch_size = os.getenv("batch_size")
processes = os.getenv("processes")
events_day_limit = os.getenv("events_day_limit")

conn_str = (
    f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"
)


batches = total_events // batch_size


def batch_insert_users(batch_size: int):
    users = generate_users(batch_size)
    sql = load_sql_file("queries/insert_users_into_users.sql")
    insert_data_into_db(conn_str, sql, users)


def batch_insert_events(batch_size: int, action_start_timestamp: int):
    events = generate_event(batch_size, action_start_timestamp)
    sql = load_sql_file("queries/insert_events_into_users_activity.sql")
    insert_data_into_db(conn_str, sql, events)


def process_all_users():
    logging.info(f"Starts of processing users")
    start = time.time()

    with multiprocessing.Pool(processes) as pool:
        pool.map(batch_insert_users, [batch_size] * batches)
    end = time.time() - start
    logging.info(
        f"Inserting of {total_users} records into users table  took a {(end / 60):.2f} minutes"
    )


def process_all_events():
    logging.info(f"Starts of processing events")
    start = time.time()
    day_count = 0
    random_date_list = {}
    while day_count <= events_day_limit:
        start_ts = time.mktime(time.strptime(start_date, "%Y-%m-%d"))
        end_ts = time.mktime(time.strptime(end_date, "%Y-%m-%d"))
        action_start_timestamp = np.random.randint(start_ts, end_ts)
        date_representation = time.strftime(
            "%Y-%m-%d", time.localtime(action_start_timestamp)
        )
        if action_start_timestamp not in random_date_list:
            random_date_list[action_start_timestamp] = date_representation

            args_list = [(batch_size, action_start_timestamp) for _ in range(batches)]

            with multiprocessing.Pool(processes) as pool:
                pool.starmap(batch_insert_events, args_list)
            day_count += 1
        else:
            continue
    with open(user_action_days, "w") as fl:
        json.dump(random_date_list, fl, indent=4)

    end = time.time() - start
    logging.info(
        f"Inserting of 10000000 records into user_activity table took a  {(end / 60):.2f} minutes"
    )

    for _ in range(7):
        action_start_timestamp = np.random.randint(start_ts, end_ts)
        date_representation = time.strftime(
            "%Y-%m-%d", time.localtime(action_start_timestamp)
        )
        random_date_list[action_start_timestamp] = date_representation


def fetch_data_by_date(start_date: str, end_date: str, steps: str):
    sql = load_sql_file("queries/fetch_data_by_date.sql")
    step_list = steps.split(",")
    for step in step_list:
        print(f"Results for {step}")
        formatted_sql = sql.format(START_DATE=start_date, END_DATE=end_date, STEP=step)
        results = execute_sql_query(formatted_sql, return_result=True)
        for result in results:
            print(f"Start of Period: {result[0]}, User Count: {result[1]}")


if __name__ == "__main__":
    create_db()
    create_tables()
    process_all_users()
    process_all_events()
    create_partition_on_user_action()
    # create_indexes()
    process_segment("queries/insert_segment_a_into_sampled_activity.sql")
    process_segment("queries/insert_segment_b_into_sampled_activity.sql")
    if len(sys.argv) != 4:
        print("Usage: python main.py <start_date> <end_date> <steps>")
        print("Example: python your_script.py 20240401 20240501 day,week,month")
    else:
        start_date = sys.argv[1]
        end_date = sys.argv[2]
        steps = sys.argv[3]
        fetch_data_by_date(start_date, end_date, steps)
