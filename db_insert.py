import logging
import os
import sys

import pyodbc
from dotenv import load_dotenv

load_dotenv()

database = os.getenv("DB_DATABASE")
server = os.getenv("DB_SERVER")
username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
driver = os.getenv("DB_DRIVER")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    stream=sys.stdout,
)


def insert_data_into_db(conn_str: str, query: str, data: list):
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    try:
        cursor.fast_executemany = True
        cursor.executemany(query, data)
        conn.commit()
    except pyodbc.Error as e:
        logging.error(f"Failed to insert data: {e}")


def get_db_connection(database_name: str = database):
    conn_str = f"DRIVER={driver};SERVER={server};DATABASE={database_name};UID={username};PWD={password}"
    return pyodbc.connect(conn_str, autocommit=True)


def execute_sql_query(
    sql: str, database_name: str = database, return_result: bool = False
) -> list or None:
    try:
        with get_db_connection(database_name) as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql)
                if return_result:
                    results = cursor.fetchall()
                    conn.commit()
                    return results
                conn.commit()
    except Exception as e:
        logging.error(f"Query {sql} filed: {e}")
        raise
