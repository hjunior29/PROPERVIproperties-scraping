import requests
from bs4 import BeautifulSoup
import utils
import json
import logging
from dotenv import load_dotenv
import os

def get_properties_data():
    
    try:
        response = requests.get(os.getenv('URL_ZAPIMOVEIS'), headers=utils.headers.get_basic_headers())
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:

        logging.error(f"Error accessing URL: {e}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    address_tags = soup.find_all(class_='l-text l-u-color-neutral-28 l-text--variant-heading-small l-text--weight-medium card__address')
    addresses = [tag.get_text(strip=True) for tag in address_tags]

    listing_price_divs = soup.find_all('div', class_='listing-price')
    prices_tags = [div.find('p', class_='l-text l-u-color-neutral-28 l-text--variant-heading-small l-text--weight-bold undefined') for div in listing_price_divs]
    prices = [int(tag.get_text(strip=True).replace("R$ ", "").replace(".", "")) for tag in prices_tags if tag]

    utils.db_request.add_properties(utils.convert.list_to_dic(addresses, prices))

    return addresses, prices

