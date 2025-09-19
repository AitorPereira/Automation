import os
import json
import re
import requests
from datetime import datetime
from bs4 import BeautifulSoup

class PriceNotifier:
    def __init__(self, products_file="tracked_products.json"):
        self.products_file = products_file

    def get_prices(self, url, selector_css=None, thousands_separator=','):
        """ Extracts product prices from a website. """

        try:
            headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9,es;q=0.8'
            }

            respond = requests.get(url, headers=headers, timeout=10)

            if respond.status_code != 200:
                return None

            soup = BeautifulSoup(respond.text, 'html.parser')

            # Search for the price using the given selector or common selectors
            element_price = None
            if selector_css:
                element_price = soup.select_one(selector_css)
            else:
                #Add as many common selectors as needed. Each website has its own
                #Mercado Libre: ':andes-money-amount__fraction'
                common_selectors = [
                    '.price', '.product-price', '.offer-price', '.current-price', '[itemprop="price"]', '.price-value', '.price-current', '.money',
                    '.a-price', '.a-price-whole', '.a-offscreen', '#priceblock_ourprice', '#priceblock_dealprice', '.andes-money-amount__fraction'
                ]

                for selector in common_selectors:
                    element_price = soup.select_one(selector)
                    if element_price:
                        break
            
            if not element_price:
                return None

            text_price = element_price.text.strip()

            #Manage the thousands separator
            if thousands_separator == '.':
                text_price = text_price.replace('.','')
                text_price = text_price.replace(',','.')
            else:
                text_price = text_price.replace(',','.')
            
            #Extract the number
            cleaned_price = re.sub(r'[^\d.]', '', text_price)
            match = re.search(r'\d+\.\d+|\d+', text_price)

            return float(match.group()) if match else None

        except Exception as e:
            return None
        
    def load_product(self):
        """ Loads the tracked products list from the file """
        if os.path.exists(self.products_file):
            try:
                with open(self.products_file, 'r', encoding='utf-8') as file:
                    return json.load(file)
            except Exception:
                pass
        
        return []

    def save_product(self, products):
        """ Saves the tracked products list to the file """
        try:
            with open(self.products_file, 'w', encoding='utf-8') as file:
                json.dump(products, file, indent=4, ensure_ascii=False)
            return True
        except Exception:
            return False

    def add_product(self, name, url, target_price, selector_css=None, thousands_separator=','):
        """ Adds a new product to the tracked products list """
        products = self.load_product()

        #Verify if the product already exists
        for product in products:
            if product['url'] == url:
                return "Product already exists"
        
        #Get actual price
        current_price = self.get_prices(url, selector_css, thousands_separator)

        #Verify if the product already exists
        new_product = {
            'name' : name,
            'url' : url,
            'target_price' : target_price,
            'selector_css' : selector_css,
            'thousands_separator' : thousands_separator,
            'added_date' : datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'current_price': current_price if current_price else None,
            'price_history' : []
        }

        if current_price is not None:
            new_product['price_history'].append({
                'date' : datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'price' : current_price
            })

        products.append(new_product)
        self.save_product(products)

        return True

    def refresh_price(self):
        """ Refreshes the prices of all tracked products """

        products = self.load_product()
        refreshed_products = []

        for product in products:
            thousands_separator = product.get('thousands_separator', ',')
            current_price = self.get_prices(product['url'], product.get('selector_css'), thousands_separator)

            if current_price is not None:
                previous_price = product.get('current_price')
                product['current_price'] = current_price

                #Add to price history
                product['price_history'].append({
                    'date' : datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'price' : current_price
                })

                #Limit the price history to the last 30 entries
                if len(product['price_history']) > 30:
                    product['price_history'] = product['price_history'][-30:]

                #In case you need to verify if the price has dropped or reached the target price
                """ if (current_price is not None and current_price < previous_price) or \
                    (current_price <= product['target_price']):
                    refreshed_products.append(product) """

                #Or verify only if the price has reached the target price
                if (current_price <= product['target_price']):
                    refreshed_products.append(product)

        self.save_product(products)
        return refreshed_products

    def remove_product(self, index):
        """ Removes a product from the tracked products list """
        products = self.load_product()

        if not products or index < 1 or index > len(products):
            return False
        
        products.pop(index -1)
        self.save_product(products)
        return True
