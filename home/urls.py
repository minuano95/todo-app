from xml.etree.ElementInclude import include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_task/', views.create_task, name='create_task'),
    path('validate_task/', views.validate_form, name='validate_form'),
    path('edit_task/', views.edit_task, name='edit_task'),
]
