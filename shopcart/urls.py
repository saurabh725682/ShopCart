from django.urls import path
from shopcart import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path('checkout/', views.checkout, name='Checkout'),
    path('handlerequest/', views.handlerequest, name='handlerequest'),
    
]
