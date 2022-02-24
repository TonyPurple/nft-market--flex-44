from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import random
import datetime

# class User(models.Model):
#     user_id = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=100)
#     password = models.CharField(max_length=50)

# class Wallet(models.Model):
#     wallet_id = models.AutoField(primary_key=True)
#     balance = models.FloatField(default=0.0)

# class Account(models.Model):
#     account_id = models.AutoField(primary_key=True)
#     username = models.ForeignKey(User, on_delete = models.CASCADE, null =False)
#     wallet = models.ForeignKey(Wallet, on_delete = models.CASCADE)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)

# class NFT_Collection(models.Model):
#     nft_collection_id = models.AutoField(primary_key=True)
#     collection_name = models.CharField(max_length=30)
#     creator = models.CharField(max_length=50)
#     # profile_pic = models.ImageField(upload_to='nftpictures')
#     description = models.TextField(blank=True)
#     owner = models.ForeignKey(Account, on_delete = models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

def random_token():
    return int(random.randint(10000, 99999))
    
class NFT(models.Model):
    id = models.AutoField(primary_key=True)
    nft_name = models.CharField(("NFT Name"),max_length=50)
    token_id = models.IntegerField(default=random_token)
    # supply = models.IntegerField
    blockchain = models.CharField(max_length=10)
    description = models.TextField(blank=True)
    # collection_name = models.ForeignKey(NFT_Collection, on_delete = models.CASCADE)
    # nft_image = models.ImageField(upload_to='nftpictures')
        # Add the foreign key linking to a user instance
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nft_name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'nft_id': self.id})

class Bid(models.Model):
  date = models.DateField(("Date"), default=datetime.date.today)
  bidprice = models.DecimalField(("Bid Price"),max_digits=8, decimal_places=3)
  nft = models.ForeignKey(NFT, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_bidprice_display()} on {self.date}"
    
  class Meta:
    ordering = ('-bidprice',)

class Sell(models.Model):
  sale_ends = models.DateField(("Date Sale Ends"))
  minbidprice = models.DecimalField(("Minimum Bid Price"),max_digits=8, decimal_places=3)
  nft = models.ForeignKey(NFT, on_delete=models.CASCADE)

class Photo(models.Model):
    url = models.CharField(max_length=200)
    nft = models.ForeignKey(NFT, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for nft_id: {self.nft_id} @{self.url}"
# class Nft_Bid(models.Model):
#     nft_bid_id = models.AutoField(primary_key=True)
#     bidder_account_id = models.ForeignKey(Account, on_delete = models.CASCADE)
#     nft_id = models.ForeignKey(NFT, on_delete = models.CASCADE)
#     offer = models.IntegerField
#     sale_ends = models.DateTimeField
#     min_bid_price = models.IntegerField