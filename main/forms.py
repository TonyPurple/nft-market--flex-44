from django.forms import ModelForm
from .models import Bid, Sell

class BidForm(ModelForm):
  class Meta:
    model = Bid
    fields = ['bidprice']

class SellForm(ModelForm):
  class Meta:
    model = Sell
    fields = ['minbidprice']