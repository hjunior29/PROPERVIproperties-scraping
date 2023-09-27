import sys
import scrapers

def main():

    locations = scrapers.zapimoveis.get_property_locations()

    for location in locations:
        print(location)

if __name__ == "__main__":
    main()
