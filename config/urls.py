from django.contrib import admin
from django.urls import path, include
from core import views
from config import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('cotacao/', views.cotacao_view, name='cotacao'),
]
