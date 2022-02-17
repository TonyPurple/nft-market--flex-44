from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
# Import the login_required decorator
from django.contrib.auth.decorators import login_required
# Import the mixin for class-based views
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3
from .models import NFT, Photo

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'nftmarketgallery'

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
  fields = ['nft_name', 'token_id', 'blockchain', 'description']
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

@login_required
def nft_detail(request, nft_id):
  nft = NFT.objects.get(id=nft_id)
  return render(request, 'nfts/detail.html', { 'nft': nft })

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