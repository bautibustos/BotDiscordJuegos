import requests, json

url_tiendas =requests.get("https://www.cheapshark.com/api/1.0/stores")

URL = requests.get(f"https://www.cheapshark.com/api/1.0/deals?storeID={idtienda}&lowerPrice=1")

