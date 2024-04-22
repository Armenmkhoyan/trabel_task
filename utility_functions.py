import json
import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    stream=sys.stdout,
)


def load_sql_file(filename: str):
    with open(filename, "r") as file:
        return file.read()


def load_json_file(path: str):
    try:
        with open(path, "r") as file:
            data = json.load(file)
            return data
    except Exception as e:
        logging.info(f"An error occurred during loading file {path}: {e}")
