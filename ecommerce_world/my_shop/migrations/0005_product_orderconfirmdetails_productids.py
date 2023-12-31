# Generated by Django 4.2.6 on 2023-10-27 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_shop', '0004_orderconfirmdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductId', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='orderconfirmdetails',
            name='ProductIds',
            field=models.ManyToManyField(to='my_shop.product'),
        ),
    ]
