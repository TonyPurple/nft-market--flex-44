from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('accounts/signup/', views.signup, name='signup'),
  path('nfts/create/', views.NFTCreate.as_view(), name='nft_create'),
  path('nfts/<int:nft_id>/', views.nft_detail, name='detail'),
  path('nfts/', views.nft_index, name='nft_index'),
  path('nfts/all/', views.NFTList.as_view(), name='nft_list'),
  path('nfts/<int:pk>/edit/', views.NFTEdit.as_view(), name='nft_edit'),
  path('nfts/<int:nft_id>/add_photo/', views.add_photo, name='add_photo'),
  path('nfts/<int:pk>/delete/', views.NFTDelete.as_view(), name='nft_delete'),
  path('nfts/<int:nft_id>/add_bid/', views.add_bid, name='add_bid'),
  path('nfts/search_result/', views.search_result, name='search_result'),
  path('nfts/<int:nft_id>/add_sell/', views.sell, name='sell'),
  path('nfts/for_sale', views.all_for_sale, name='for_sale'),
  path('like/<int:pk>', views.likeview, name='like_nft'),
]