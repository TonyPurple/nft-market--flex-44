from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('accounts/signup/', views.signup, name='signup'),
  path('nft/<int:nft_id>/', views.nft_detail, name='detail'),
  path('nft/create/', views.NFTCreate.as_view(), name='nft_create'),
]