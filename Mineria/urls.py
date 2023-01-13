from django.urls import path

from Mineria.views import saludar,lista_minerales

urlpatterns = [
    path('saludar/', saludar),
    path('lista_minerales/', lista_minerales),
]
