import logging
import os
import sys

from dotenv import load_dotenv

from db_setup import execute_sql_query
from utility_functions import load_json_file, load_sql_file

load_dotenv()

user_action_days = os.getenv("USER_ACTION_DAYS")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    stream=sys.stdout,
)


def process_segment(segment_sql_path: str):
    insert_into_sampled_activity_segment = load_sql_file(segment_sql_path)
    data = load_json_file(user_action_days)
    action_days = list(data)

    insert_user_id_into_temp_segment = load_sql_file(
        "queries/insert_user_id_into_temp.sql"
    )
    for date in action_days:
        formatted_insert_into_sampled_activity_segment = (
            insert_into_sampled_activity_segment.format(date=date)
        )
        formatted_insert_user_id_into_temp_segment = (
            insert_user_id_into_temp_segment.format(date=date)
        )
        execute_sql_query(formatted_insert_into_sampled_activity_segment)
        logging.info(
            "Inserting of 2000 users into sampled_activity_data successfully done."
        )
        execute_sql_query(formatted_insert_user_id_into_temp_segment)
        logging.info("Inserting of users into temp table successfully done.")
