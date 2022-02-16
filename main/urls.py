from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('accounts/signup/', views.signup, name='signup'),
  path('nfts/create/', views.NFTCreate.as_view(), name='nft_create'),
  path('nfts/<int:nft_id>/', views.nft_detail, name='detail'),
  path('nfts/', views.nft_index, name='nft_index'),
]