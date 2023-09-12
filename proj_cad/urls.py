from django.urls import path
from app_cad_users import views

urlpatterns = [
    path('', views.home, name='home'),
    path('users/', views.users, name='users'),
]
