from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
# Import the login_required decorator
from django.contrib.auth.decorators import login_required
# Import the mixin for class-based views
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import NFT
# Create your views here.
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