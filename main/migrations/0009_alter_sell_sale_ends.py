# Generated by Django 4.0.1 on 2022-02-23 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_bid_bidprice_alter_nft_nft_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sell',
            name='sale_ends',
            field=models.DateField(verbose_name='Date Sale Ends'),
        ),
    ]