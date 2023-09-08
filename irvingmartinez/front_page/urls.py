from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='front_page-home')
]
