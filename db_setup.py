import sys
import os
import logging
from dotenv import load_dotenv

from db_insert import execute_sql_query
from utility_functions import load_sql_file, load_json_file
load_dotenv()

users_activity_table = os.getenv('DB_USERS_ACTIVITY_TABLE')
user_action_days = 'user_action_days.json'

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', stream=sys.stdout)


def create_db():
    sql = load_sql_file('queries/create_db.sql')
    sql_formatted = sql.format(database='Trabel2')
    execute_sql_query(sql_formatted, 'master')
    logging.info("Database successfully created")


def create_tables():
    sql = load_sql_file('queries/create_tables.sql')
    sql_commands = sql.split('GO')
    for command in sql_commands:
        if command.strip():
            execute_sql_query(command)
            logging.info(f"Query {command} executed successfully")


def create_partition_on_user_action():
    data = load_json_file(user_action_days)
    timestamps = list(data.keys())
    values_clause = ", ".join(timestamps)
    table_name = users_activity_table
    index_column = 'device_time'
    sql = load_sql_file('queries/create_partition_on_user_action_table.sql')
    sql_formatted = sql.format(values_clause=values_clause, table_name=table_name, index_column=index_column)
    execute_sql_query(sql_formatted)
