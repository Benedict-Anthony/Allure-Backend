# Generated by Django 4.1.5 on 2023-03-12 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_ordereditems_transaction_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordereditems',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
