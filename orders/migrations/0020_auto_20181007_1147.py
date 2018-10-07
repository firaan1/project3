# Generated by Django 2.0.3 on 2018-10-07 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0019_auto_20181007_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placedorder',
            name='orderdinnerplatter',
            field=models.ManyToManyField(related_name='order_dinnerplatter', to='orders.OrderDinnerPlatter'),
        ),
        migrations.AlterField(
            model_name='placedorder',
            name='orderpasta',
            field=models.ManyToManyField(related_name='order_pasta', to='orders.OrderPasta'),
        ),
        migrations.AlterField(
            model_name='placedorder',
            name='orderpizza',
            field=models.ManyToManyField(related_name='order_pizza', to='orders.OrderPizza'),
        ),
        migrations.AlterField(
            model_name='placedorder',
            name='ordersalad',
            field=models.ManyToManyField(related_name='order_salad', to='orders.OrderSalad'),
        ),
        migrations.AlterField(
            model_name='placedorder',
            name='ordersub',
            field=models.ManyToManyField(related_name='order_sub', to='orders.OrderSub'),
        ),
    ]
