# Generated by Django 4.0.2 on 2022-02-16 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_alter_order_totalcost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='totalCost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
    ]