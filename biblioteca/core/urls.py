<<<<<<< HEAD
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('listar', views.listar, name='listar'),
]
=======
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('listar', views.listar, name='listar'),
]
>>>>>>> 89d95d6168a52ef6ca3eed0cc40ea59491c33c66
