# Generated by Django 4.2.6 on 2023-10-27 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_shop', '0005_product_orderconfirmdetails_productids'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productbuydetails',
            name='ProductIds',
        ),
        migrations.AddField(
            model_name='productbuydetails',
            name='ProductIds',
            field=models.ManyToManyField(to='my_shop.product'),
        ),
    ]
