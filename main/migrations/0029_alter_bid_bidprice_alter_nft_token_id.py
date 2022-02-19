# Generated by Django 4.0.1 on 2022-02-19 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_alter_nft_token_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bidprice',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='nft',
            name='token_id',
            field=models.IntegerField(default=70012, max_length=5),
        ),
    ]
