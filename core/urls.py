from django.urls import path, include

from core import views
from config import views


urlpatterns = [
    path('', views.index, name='home'),
    path('cotacao/', views.cotacao_view, name='cotacao'),
]