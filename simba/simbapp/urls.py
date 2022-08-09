from django.urls import path
from simbapp import views


urlpatterns = [
    path('', views.index, name='index'),
    path('homepage/maps/', views.map),
    path('homepage/chat/', views.chat),
    path('search/', views.search),
    path('settings/', views.settings),
    path('signin/', views.signin),
    path('register/', views.register),
    path('signout/', views.signout),
    path('homepage/', views.homepage)
    
] 