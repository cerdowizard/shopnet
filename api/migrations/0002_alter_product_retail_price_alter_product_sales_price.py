# Generated by Django 4.2.1 on 2023-09-14 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='retail_price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='sales_price',
            field=models.IntegerField(),
        ),
    ]