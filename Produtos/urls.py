from django.urls import path
from Produtos import views


urlpatterns = [
    path('', views.Produtos, name='produtos'),
    path('infoprod/<int:id>', views.ViewProd, name='infoprod'),

]



