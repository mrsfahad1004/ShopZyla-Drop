"""
lister.py
Lists products to your Shopify/ShopZyla store using API requests.
"""

import requests
from config import SHOP_API_URL, SHOPZYLA_API_KEY

def list_product(product):
    """
    List a single product to your Shopify/ShopZyla store.
    Returns status code and response text for logging.
    """
    payload = {
        "title": product.get("title", ""),
        "price": product.get("price", ""),
        "description": product.get("description", "")
    }
    
    headers = {"Authorization": f"Bearer {SHOPZYLA_API_KEY}"}
    
    try:
        response = requests.post(SHOP_API_URL, json=payload, headers=headers)
        if response.status_code in [200, 201]:
            print(f"Successfully listed: {product['title']}")
        else:
            print(f"Failed to list: {product['title']} - Status: {response.status_code}")
        return response.status_code, response.text
    except requests.RequestException as e:
        print(f"Error listing product {product['title']}: {e}")
        return None, str(e)
