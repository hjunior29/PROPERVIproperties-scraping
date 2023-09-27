import json

def list_to_dic(addresses, prices):
    return [{"address": address, "price": price} for address, price in zip(addresses, prices)]
