from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from .models import NFT, Photo, Sell
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
# Import the login_required decorator
from django.contrib.auth.decorators import login_required
# Import the mixin for class-based views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from .forms import BidForm, SellForm
import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'nftmarketgallery'

@login_required
def add_photo(request, nft_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}/{BUCKET}/{key}"
            photo = Photo(url=url, nft_id=nft_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
        return redirect('detail', nft_id=nft_id)

class NFTCreate(LoginRequiredMixin, CreateView):
  model = NFT
  fields = ['nft_name','description']
  def get_success_url(self):
        return reverse('detail', kwargs={'nft_id': self.object.id})
  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)

class NFTEdit(LoginRequiredMixin, UpdateView):
  model = NFT
  fields = ['nft_name', 'description']
  def get_success_url(self):
    return reverse('detail', kwargs={'nft_id': self.object.id})
  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)

class NFTDelete(LoginRequiredMixin, DeleteView):
  model = NFT
  success_url='/nfts/'

class NFTList(ListView):
  model = NFT

@login_required
def add_bid(request, nft_id):
  form = BidForm(request.POST)
  if form.is_valid():
    new_bid = form.save(commit=False)
    new_bid.nft_id = nft_id
    new_bid.save()
  return redirect('detail', nft_id=nft_id)


@login_required
def nft_detail(request, nft_id):
  nft = NFT.objects.get(id=nft_id)
  bid_form = BidForm()
  return render(request, 'nfts/detail.html', { 'nft': nft, 'bid_form':bid_form})
  template_name = 'detail.html'

def get_context_data(self, *args, **kwargs):
    stuff = get_object_or_404(NFT, id=self.kwargs['pk'])
    total_likes = stuff.total_likes()
    context["total_likes"] = total_likes
    return context

def likeview(request, pk):

  nft = get_object_or_404(NFT, pk=pk)
  nft.likes.add(request.user)
  return HttpResponseRedirect(reverse('detail', args=[str(pk)]))

@login_required
def nft_index(request):
  nfts = NFT.objects.filter(user=request.user)
  # nfts = NFT.objects.all()
  return render(request, 'nfts/index.html', { 'nfts': nfts }) 

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def home(request):
  return render(request, 'home.html')

def search_result(request):
  if request.method == "GET":
    searched = request.GET['searched']
    search_result = NFT.objects.filter(nft_name__contains=searched)
    return render(request, 'main/nft_search_result.html', {'searched': searched, 'search_result':search_result})
  else:
    return render(request, 'main/nft_search_result.html')

@login_required
def sell(request, nft_id):
  form = SellForm(request.POST)
  if form.is_valid():
    new_sell = form.save(commit=False)
    new_sell.nft_id = nft_id
    new_sell.save()
    return redirect('detail', nft_id=nft_id)
  return render(request, 'main/sell_form.html', { 'nft': nft_id,'form':form})

def all_for_sale(request):
  nft = NFT.objects.all()
  return render(request, 'nfts/for_sale.html',{ 'nft': nft }) 
  