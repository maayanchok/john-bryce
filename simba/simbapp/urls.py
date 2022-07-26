from django.urls import path
from simbapp import views

urlpatterns = [
    path('map/',views.map),
    path('chat/', views.chat),
    path('search/', views.search),
    path('settings/', views.settings),
    path('sign_in/', views.sign_in),
    path('register/', views.register)
]
