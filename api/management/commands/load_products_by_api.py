import requests as requests
from django.core.management.base import BaseCommand
import json
from datetime import datetime, timedelta
import urllib

from api.models import Product


# def strip_url_of_query_params(url):
#     parsed = urllib.parse.urlparse(url)
#     return parsed.scheme + "://" + parsed.netloc + parsed.path

class Command(BaseCommand):
    help = 'Loads product data from a JSON file and adds them to the database'

    def get_json(self, filename):
        with open(f'product/management/commands/{filename}', 'r') as f:
            products = f.read()
            return json.loads(products)

    def handle(self, *args, **kwargs):
        self.load('nordstrom.json')
        self.load('urban_outfitters.json')

    def load(self, filename):
        products = self.get_json(filename)
        for product in products:
            product_image = product['product_image_urls']
            if 'urban_outfitters' in filename:
                product_image = product_image

            # Check if product already exists in the database
            existing_product = Product.objects.filter(product_name=product['product_name']).first()
            if existing_product:
                # update the product timestamp
                existing_product.timestamp = datetime.now()
                existing_product.save()
                print(f"Product {product['product_name']} already exists. Timestamp updated.")
            else:
                payload = {
                    'category': None,
                    'product_url': product['product_url'],
                    'brand': product['brand'],
                    'product_name': product['product_name'],
                    'sales_price': Product.sanitize_price(product['sales_price']),
                    'retail_price': Product.sanitize_price(product['retail_price']),
                    'product_image_urls': product_image
                }
                product = Product.create_product(payload, product_loaded_by=Product.AUTO_SCRAPED)
                print(f"Loaded {product.product_id}.")
                headers = {
                    'Inner-Http-Authorization': 'Bearer SECRET-903-KDLJFDAABACKDLAFJEIFJ',
                    'Content-Type': 'application/json',
                }
                response = requests.post('http://127.0.0.1:8000/products/create', json=payload, headers=headers)
                if not str(response.status_code).startswith('2'):
                    print(f"NO: {response.status_code}")
                    print(f"Pass: {response.content}")
                else:
                    print(f"Yay: {response.status_code}")
