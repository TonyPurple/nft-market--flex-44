from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import random
import datetime


def random_token():
    return int(random.randint(10000, 99999))
    
class NFT(models.Model):
    id = models.AutoField(primary_key=True)
    nft_name = models.CharField(("NFT Name"),max_length=50)
    token_id = models.IntegerField(default=random_token)
    blockchain = models.CharField(max_length=10)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.nft_name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'nft_id': self.id})

class Bid(models.Model):
  date = models.DateField(("Date"), default=datetime.date.today)
  bidprice = models.FloatField(("Bid Price"))
  nft = models.ForeignKey(NFT, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_bidprice_display()} on {self.date}"
    
  class Meta:
    ordering = ('-bidprice',)

class Sell(models.Model):
  sale_ends = models.DateField(("Date Sale Ends"))
  minbidprice = models.FloatField(("Minimum Bid Price (in ETH)"))
  nft = models.ForeignKey(NFT, on_delete=models.CASCADE)

class Photo(models.Model):
    url = models.CharField(max_length=200)
    nft = models.ForeignKey(NFT, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for nft_id: {self.nft_id} @{self.url}"
