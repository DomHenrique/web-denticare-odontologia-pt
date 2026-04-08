from django.urls import path
from .views import RegistroView, fazer_logout, fazer_login


urlpatterns = [
    path('', RegistroView.as_view(), name='autenticacao'),

    path('logout/', fazer_logout, name='logout'),
    path('login/', fazer_login, name='login'),
]


