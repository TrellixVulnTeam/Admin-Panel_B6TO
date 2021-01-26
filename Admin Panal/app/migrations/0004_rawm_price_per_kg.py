# Generated by Django 3.1.5 on 2021-01-25 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_supplier_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='rawm',
            name='price_per_Kg',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]