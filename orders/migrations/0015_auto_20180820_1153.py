# Generated by Django 2.0.3 on 2018-08-20 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_auto_20180820_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placedorder',
            name='totalprice',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
