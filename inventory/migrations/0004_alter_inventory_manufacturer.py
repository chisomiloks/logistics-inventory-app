# Generated by Django 4.0.1 on 2022-01-17 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_inventory_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='manufacturer',
            field=models.CharField(default='N/A', max_length=50),
        ),
    ]
