# Generated by Django 5.1 on 2024-09-07 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0003_trade_order_type_trade_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='order_type',
            field=models.CharField(choices=[('Market', 'Market'), ('Limit', 'Limit'), ('Stop', 'Stop'), ('Trailing Stop', 'Trailing Stop'), ('GTC', 'Good Till Cancelled'), ('FOK', 'Fill or Kill')], default='Market', max_length=20),
        ),
        migrations.AlterField(
            model_name='trade',
            name='quantity',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
