# Generated by Django 5.0.1 on 2024-03-13 22:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_alter_listing_categories_alter_listing_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='categories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listings', to='auctions.category'),
        ),
    ]
