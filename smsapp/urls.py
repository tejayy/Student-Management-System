from django.urls import path
from smsapp import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('', views.login_view, name='login'),
    
]