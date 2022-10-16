from django.urls import path
from . import views 

app_name = 'listing'
urlpatterns = [
    path('', views.listing_list, name='listing_list'),
    path('retrieve/<int:pk>/', views.listing_retrieve, name='retrieve'),
    path('create/', views.listing_create, name='create'),
    path('retrieve/<int:pk>/update/', views.listing_update, name='update'),
    path('retrieve/<int:pk>/delete/', views.listing_delete, name='delete'),
]