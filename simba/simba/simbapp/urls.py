from django.urls import path
from simbapp import views


urlpatterns = [
    path('', views.homepage),
    path('map/', views.map),
    path('chat/', views.chat),
    path('search/', views.search),
    path('settings/', views.settings),
    path('signin/', views.signin),
    path('register/', views.register),
    
] 