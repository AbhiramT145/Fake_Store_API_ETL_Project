import pandas as pd
import requests
from logger import logger

BASE_URL = "https://fakestoreapi.com/"

def extract_product():
    url = f'{BASE_URL}/products'

    logger.info("Starting product extraction.")

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()
        product_df = pd.DataFrame(data)

        logger.info(f"Successfully extracted {len(product_df)} products.")

        return product_df

    except requests.exceptions.RequestException:
        logger.exception("Failed to extract product data.")
        raise

def extract_users():
    url = f'{BASE_URL}/users'

    logger.info("Starting user extraction.")

    try:

        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        user_df = pd.DataFrame(data)

        logger.info(f"Successfully extracted {len(user_df)} users.")
        
        return user_df
    except requests.exceptions.RequestException:
        logger.exception("Failed to extract user data.")
        raise
