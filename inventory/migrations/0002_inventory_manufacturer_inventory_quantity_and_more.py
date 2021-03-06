# Generated by Django 4.0.1 on 2022-01-17 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='manufacturer',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='inventory',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='title',
            field=models.CharField(default='', max_length=50),
        ),
    ]
