# Generated by Django 2.1.5 on 2019-01-26 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20190126_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfoliomodel',
            name='currency',
            field=models.CharField(blank=True, default=None, max_length=4, null=True),
        ),
    ]
