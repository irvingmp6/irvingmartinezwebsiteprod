from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='front_page-home'),
    path('admin/', views.dont_do_that, name='front_page-dont-do-that')
]
