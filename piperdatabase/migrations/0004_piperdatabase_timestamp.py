# Generated by Django 2.1.5 on 2019-01-25 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piperdatabase', '0003_auto_20190123_0019'),
    ]

    operations = [
        migrations.AddField(
            model_name='piperdatabase',
            name='timestamp',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
