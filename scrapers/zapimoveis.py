import requests
from bs4 import BeautifulSoup
import utils

def get_property_locations():
    
    url = "https://www.zapimoveis.com.br/venda/imoveis/go+goiania/?__ab=exp-aa-test:control,new-discover-zap:alert,vas-officialstore-social:enabled&transacao=venda&onde=,Goi%C3%A1s,Goi%C3%A2nia,,,,,city,BR%3EGoias%3ENULL%3EGoiania,-16.686891,-49.264794,&pagina=1"
    
    try:
        response = requests.get(url, headers=utils.headers.get_basic_headers())
        response.raise_for_status()
        print(response)
    except requests.exceptions.HTTPError as e:
        print(f"Error accessing URL:\n {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    address_tags = soup.find_all(class_='l-text l-u-color-neutral-28 l-text--variant-heading-small l-text--weight-medium card__address')
    print(address_tags)

    addresses = [tag.get_text(strip=True) for tag in address_tags]
    print(addresses)

    return addresses

