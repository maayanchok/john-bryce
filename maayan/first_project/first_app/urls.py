from django.urls import path
from first_app import views

urlpatterns = [
    path('',views.index_2,name="index_2")
]