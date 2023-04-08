from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('contact', views.contact, name='contact'),
    path('service', views.service, name='service'),
    path('new_user', views.new_user, name='new_user'),
    path('user', views.user, name='user'),

]
