from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

class Wallet(models.Model):
    wallet_id = models.AutoField(primary_key=True)
    balance = models.FloatField(default=0.0)

class Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    username = models.ForeignKey(User, on_delete = models.CASCADE, null =False)
    wallet = models.ForeignKey(Wallet, on_delete = models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class NFT_Collection(models.Model):
    nft_collection_id = models.AutoField(primary_key=True)
    collection_name = models.CharField(max_length=30)
    creator = models.CharField(max_length=50)
    # profile_pic = models.ImageField(upload_to='nftpictures')
    description = models.TextField(blank=True)
    owner = models.ForeignKey(Account, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class NFT(models.Model):
    nft_id = models.AutoField(primary_key=True)
    nft_name = models.CharField(max_length=50)
    token_id = models.IntegerField
    supply = models.IntegerField
    description = models.TextField(blank=True)
    collection_name = models.ForeignKey(NFT_Collection, on_delete = models.CASCADE)
    blockchain = models.CharField
    # nft_image = models.ImageField(upload_to='nftpictures')

class Nft_Bid(models.Model):
    nft_bid_id = models.AutoField(primary_key=True)
    bidder_account_id = models.ForeignKey(Account, on_delete = models.CASCADE)
    nft_id = models.ForeignKey(NFT, on_delete = models.CASCADE)
    offer = models.IntegerField
    sale_ends = models.DateTimeField
    min_bid_price = models.IntegerField