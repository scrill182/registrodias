

from django.urls import path
from . import views


urlpatterns = [
    path('', views.regdaysview, name='registrodiasfest'),
    path('detalle/<int:pk>/', views.detalle_registro, name='detalle_registro'),
    path('registro/new/', views.reg_new, name='reg_new'),

]