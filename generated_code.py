import requests
from bs4 import BeautifulSoup
from typing import Dict, List
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ProductPriceScraper:
    def __init__(self, url: str) -> None:
        """
        Initialize the scraper with the URL of the e-commerce page.

        Args:
            url (str): The URL of the e-commerce page.
        """
        self.url = url
        self.headers = {'User-Agent': 'Mozilla/5.0'}  # Add a user-agent header

    def extract_prices(self) -> Dict[str, List[str]]:
        """
        Extract product prices from the e-commerce page.

        Returns:
            Dict[str, List[str]]: A dictionary with product names as keys and a list of prices as values.
        """
        try:
            # Send a GET request to the URL with headers
            response = requests.get(self.url, headers=self.headers)
            response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes

            # Check if the response is not empty
            if response.content:
                # Parse the HTML content using BeautifulSoup
                soup = BeautifulSoup(response.content, 'html.parser')
                product_info = soup.find_all('div', {'class': 'product-info'})

                # Extract product names and prices
                products = {}
                for product in product_info:
                    # Use try-except block to handle potential errors
                    try:
                        name = product.find('h2', {'class': 'product-name'}).text.strip()
                        price = product.find('span', {'class': 'price'}).text.strip()
                        products[name] = [price]
                    except AttributeError:
                        logger.error(f"Error extracting product info: {product}")
                        continue

                return products
            else:
                logger.error("Response is empty")
                return {}
        except requests.exceptions.RequestException as e:
            logger.error(f"Request error: {e}")
            return {}
        except Exception as e:
            logger.error(f"Error: {e}")
            return {}

# Example usage
if __name__ == "__main__":
    # Create an instance of the scraper
    scraper = ProductPriceScraper('https://example.com/products')

    # Extract product prices
    prices = scraper.extract_prices()

    # Print the extracted prices
    for product, price_list in prices.items():
        logger.info(f"Product: {product}")
        for price in price_list:
            logger.info(f"Price: {price}")