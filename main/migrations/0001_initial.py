# Generated by Django 4.0.1 on 2022-02-22 23:50

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NFT',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nft_name', models.CharField(max_length=50)),
                ('token_id', models.IntegerField(default=10475, max_length=5)),
                ('blockchain', models.CharField(max_length=10)),
                ('description', models.TextField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('nft', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.nft')),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('bidprice', models.DecimalField(decimal_places=3, max_digits=8)),
                ('nft', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.nft')),
            ],
        ),
    ]
