from django.urls import path
from . import views


urlpatterns = [
    path('', views.comhome, name='comhome'),
    path('create', views.create, name='create')
]
