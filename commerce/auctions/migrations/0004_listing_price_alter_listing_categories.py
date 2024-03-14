# Generated by Django 5.0.1 on 2024-03-13 19:28

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_remove_category_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.00, max_digits=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listing',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='listings', to='auctions.category'),
        ),
    ]
