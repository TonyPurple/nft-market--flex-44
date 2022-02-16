from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import NFT
# Create your views here.
class NFTCreate(CreateView):
  model = NFT
  fields = ['nft_name', 'token_id', 'blockchain', 'description']
  success_url='/'
  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)

def nft_detail(request, nft_id):
  nft = NFT.objects.get(id=nft_id)
  return render(request, 'nfts/detail.html', { 'nft': nft })

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