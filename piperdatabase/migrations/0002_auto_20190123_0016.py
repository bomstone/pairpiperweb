# Generated by Django 2.1.5 on 2019-01-22 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('piperdatabase', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='piperdatabase',
            old_name='asset',
            new_name='symbol',
        ),
    ]
