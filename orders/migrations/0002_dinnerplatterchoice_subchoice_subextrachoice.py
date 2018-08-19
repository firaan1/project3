# Generated by Django 2.0.3 on 2018-08-19 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DinnerPlatterChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dinnerplatterchoice', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='SubChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subchoice', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='SubExtraChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subextrachoice', models.CharField(max_length=64)),
            ],
        ),
    ]
