# Generated by Django 4.0.6 on 2022-07-18 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_rename_tile_listing_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='is_publised',
            new_name='is_published',
        ),
    ]