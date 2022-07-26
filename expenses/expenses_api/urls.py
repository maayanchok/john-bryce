
from django.urls import path
from expenses_api import views


urlpatterns = [
    path('add/', views.add),
    path('display/', views.display),
    path('analysis/', views.analysis),
    path('', views.index),
]
