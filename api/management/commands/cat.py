from django.core.management.base import BaseCommand
from faker import Faker
from random import choice  # Import the 'choice' function to select from a list

from api.models import Category


class Command(BaseCommand):
    help = 'Create 20 different clothing categories for an e-commerce website'

    CLOTHING_CATEGORIES = [
        'T-shirts', 'Jeans', 'Dresses', 'Sweaters', 'Jackets',
        'Shoes', 'Hats', 'Socks', 'Pants', 'Skirts',
        'Hoodies', 'Scarves', 'Swimwear', 'Blouses', 'Shorts',
        'Outerwear', 'Activewear', 'Lingerie', 'Accessories', 'Sleepwear'
    ]

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(20):
            category_name = choice(self.CLOTHING_CATEGORIES)
            category = Category(name=category_name)
            category.save()
            self.stdout.write(self.style.SUCCESS(f"Created clothing category '{category_name}'."))

