# Generated by Django 4.0.6 on 2022-07-18 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='tile',
            new_name='title',
        ),
    ]