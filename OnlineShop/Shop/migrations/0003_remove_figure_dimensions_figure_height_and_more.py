# Generated by Django 5.0.2 on 2024-02-14 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0002_cart_cartproduct_cart_products_customer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='figure',
            name='dimensions',
        ),
        migrations.AddField(
            model_name='figure',
            name='height',
            field=models.FloatField(default=10),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Dimensions',
        ),
    ]
