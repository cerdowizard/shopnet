from django.core.management.base import BaseCommand
import json
from product.models import Product

class Command(BaseCommand):
    help = 'Delete all products.'


    def handle(self, *args, **kwargs):
        num = Product.objects.all().delete()
        print(f"Deleted: {num}")
