import requests
import utils
import logging
from dotenv import load_dotenv
import os

def add_properties(payload):

    try:
        response = requests.post(os.getenv('URL_DB_MICROSERVICE'), json=payload, headers=utils.headers.get_basic_headers())

        if response.status_code == 200:
            logging.info(response.text)
        else:
            logging.error(f"Request error: Code {response.status_code}")
            logging.error(response.text)

    except requests.exceptions.RequestException as e:
        logging.error(f"Request error: {str(e)}")

    return response
