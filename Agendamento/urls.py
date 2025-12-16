from django.urls import path
from . import views

app_name = 'Agendamento'

urlpatterns = [
    path('', views.agendar, name='index'),
    path('api/profissionais/<int:servico_id>/', views.get_profissionais, name='get_profissionais'),
    path('api/dias/', views.get_dias_disponiveis, name='get_dias_disponiveis'),
    path('api/horarios/', views.get_horarios, name='get_horarios'),
    path('confirmar/', views.confirmar_agendamento, name='confirmar_agendamento'),
]
