"""
scraper.py
Fetches products from ShopZyla API based on category.
Returns list of product dictionaries.
"""

import requests
from config import SHOPZYLA_API_KEY

def fetch_products(category="all"):
    """
    Fetch products from ShopZyla API based on category.
    Returns a list of products (dicts) or empty list if failed.
    """
    url = f"https://api.shopszyla.com/products?category={category}"
    headers = {"Authorization": f"Bearer {SHOPZYLA_API_KEY}"}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        products = response.json()
        print(f"Fetched {len(products)} products from category '{category}'.")
        return products
    except requests.RequestException as e:
        print(f"Error fetching products: {e}")
        return []
