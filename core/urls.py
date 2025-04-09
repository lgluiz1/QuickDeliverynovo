from django.urls import path, include

from core.views import  empresa,servicos,unidades,certificados,cod_etica,contato 
from config import views


urlpatterns = [
    path('', views.index, name='home'),
    path('cotacao/', views.cotacao_view, name='cotacao'),
    path('empresa/', empresa, name='empresa'),
    path('servicos/', servicos, name='servicos'),
    path('unidades/', unidades, name='unidades'),
    path('certificados/', certificados, name='certificados'),
    path('cod_etica/', cod_etica, name='cod_etica'),
    path('contato/', contato, name='contato'),
]