# Generated by Django 4.2 on 2025-02-23 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_remove_payment_order'),
        ('trading', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tradeorder',
            name='buyer',
        ),
        migrations.RemoveField(
            model_name='tradeorder',
            name='offer',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='TradeOrder',
        ),
    ]
