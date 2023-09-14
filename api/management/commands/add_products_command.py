from django.core.management.base import BaseCommand
import json
from product.models import Product

class Command(BaseCommand):
    help = 'Loads product data from a JSON file and adds them to the database'

    def add_argument(self, parser):
        parser.add_argument('product_file', type=str, help='Path to the product JSON file')

    def handle(self, *args, **kwargs):
        product_file = kwargs['product_file']
        with open(product_file) as f:
            products_data = json.load(f)
        
        add_products(products_data)

