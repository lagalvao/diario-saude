from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('visitante/', views.visitante, name='visitante'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('cadastro/', views.registroUsuario, name='cadastro'),
    path('painel/', views.painel, name='painel'),
    path('painel/editar/', views.editarUsuario, name='editar'),
    path('painel/agenda/', views.agenda, name='agenda'),
    path('painel/agenda/insereAgenda/', views.insereAgenda, name='insereAgenda'),
    path('painel/busca', views.buscaMed, name='buscaMed'),
    path('painel/cadAnalise/', views.cadAnalise, name='cadAnalise'),
    path('painel/exAnalise', views.exAnalise, name='exAnalise')
]
