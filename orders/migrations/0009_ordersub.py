# Generated by Django 2.0.3 on 2018-08-14 19:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0008_auto_20180814_1859'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderSub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subchoice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sub_choice', to='orders.SubRate')),
                ('subextra', models.ManyToManyField(related_name='sub_extra', to='orders.SubExtra')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sub_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]