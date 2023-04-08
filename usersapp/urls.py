from django.urls import path
from . import views


urlpatterns = [
    path('', views.user, name='user'),
    path('new_user/', views.new_user, name='new_user')
]
