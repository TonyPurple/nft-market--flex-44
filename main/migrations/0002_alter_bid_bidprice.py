# Generated by Django 4.0.1 on 2022-02-24 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bidprice',
            field=models.FloatField(verbose_name='Bid Price'),
        ),
    ]