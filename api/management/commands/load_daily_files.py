import json
from django.core.management.base import BaseCommand
from faker import Faker
from api.models import Product, Category

class Command(BaseCommand):
    help = 'Loads product data from a JSON file and adds them to the database'

    def get_json(self, filename):
        with open(f'api/management/commands/{filename}', 'r') as f:
            products = f.read()
            return json.loads(products)

    def handle(self, *args, **kwargs):
        self.load('nordstrom.json')
        self.load('urban_outfitters.json')

    def load(self, filename):
        products = self.get_json(filename)
        fake = Faker()

        for product in products:
            product_image = product['product_image_urls']
            if 'urban_outfitters' in filename:
                product_image = product_image
            if Product.objects.filter(title=product['product_name']).exists():
                self.stdout.write(self.style.WARNING(f"Product '{product['product_name']}' already exists."))
                continue

            # Retrieve the category based on some criteria (e.g., category name)
            category_name = product.get('category_name')  # Replace with the actual field name
            category = Category.objects.filter(name=category_name).first()

            # Generate a random price between 10 and 100 using Faker
            sales_price = fake.random_int(min=10, max=100)
            retail_price = fake.random_int(min=10, max=100)

            # Create the product and assign the category
            _product = Product(
                title=product['product_name'],
                description=fake.paragraph(),
                category=category,
                sales_price=sales_price,
                retail_price=retail_price,
                stock_quantity=fake.random_int(min=1, max=50),  # Random stock quantity
                image=product_image,  # Replace with actual image data
            )
            _product.save()
            self.stdout.write(self.style.SUCCESS(f"Loaded product '{product['product_name']}'."))
