# Generated by Django 2.2.13 on 2022-07-26 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_rename_address_listing_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
