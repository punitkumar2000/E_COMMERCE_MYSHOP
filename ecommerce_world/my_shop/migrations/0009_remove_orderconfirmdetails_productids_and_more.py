# Generated by Django 4.2.6 on 2023-10-28 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_shop', '0008_alter_orderconfirmdetails_otp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderconfirmdetails',
            name='ProductIds',
        ),
        migrations.RemoveField(
            model_name='productbuydetails',
            name='ProductIds',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.AddField(
            model_name='orderconfirmdetails',
            name='ProductIds',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='productbuydetails',
            name='ProductIds',
            field=models.CharField(max_length=200, null=True),
        ),
    ]