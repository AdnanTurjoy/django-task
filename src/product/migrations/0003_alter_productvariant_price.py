# Generated by Django 4.1.3 on 2022-11-20 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_productvariant_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productvariant',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
