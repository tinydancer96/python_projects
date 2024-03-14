# Generated by Django 5.0.1 on 2024-03-14 22:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_remove_bids_listing_alter_bids_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bids',
            name='listing',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='auctions.listing'),
        ),
        migrations.AlterField(
            model_name='bids',
            name='price',
            field=models.DecimalField(decimal_places=2, default=100, max_digits=10000),
        ),
        migrations.AlterField(
            model_name='listing',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10000),
        ),
    ]