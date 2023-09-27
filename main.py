import sys
import scrapers
import logging

def main():

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    scrapers.zapimoveis.get_property_locations()

if __name__ == "__main__":
    main()
