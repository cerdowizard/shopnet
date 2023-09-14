from django.core.management.base import BaseCommand
from django.utils import timezone
from random import uniform, choice

from product.models import Aesthetic, Product
from product.hash_urls import encrypt

class Command(BaseCommand):
    help = "Generates 50 fake products with equal distribution of price ranges and 3 aesthetics"

    def handle(self, *args, **kwargs):
        def upsert_aesthetic(name):
            aesthetic, created = Aesthetic.objects.get_or_create(
                aesthetic_name=name
            )
            return aesthetic if created else Aesthetic.objects.get(aesthetic_name=name)

        aesthetics = [
            upsert_aesthetic(aesthetic)
            for aesthetic
            in
            ["Clean Girl", "Disco", "FunkFunk"]
        ]
        categories = ['tops', 'bottoms', 'accessories']
        price_ranges = [
            (0, 25),
            (25, 50),
            (50, 100),
        ]

        for i in range(50):
            price_range = choice(price_ranges)
            sales_price = uniform(price_range[0], price_range[1])
            retail_price = sales_price * 1.4
            product_url = f"http://example.com/{i}"
            Product.objects.create(
                category=choice(categories),
                product_url=product_url,
                hashed_product_url_code=encrypt(product_url),
                brand=f"Levi's-{i}",
                aesthetic=choice(aesthetics),
                product_name=f"Product-{i}",
                sales_price=sales_price,
                retail_price=retail_price,
                sizes=None,
                product_image_urls=["shoe.jpeg"],
                is_favorited=False,
                product_loaded_by=Product.TEST_PRODUCT,
            )
