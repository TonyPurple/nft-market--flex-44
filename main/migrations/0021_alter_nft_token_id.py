# Generated by Django 4.0.1 on 2022-02-19 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_alter_nft_token_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nft',
            name='token_id',
            field=models.IntegerField(default=23347, max_length=5),
        ),
    ]