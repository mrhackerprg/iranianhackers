from django.urls import path
from . import views

app_name = 'deface'
urlpatterns = [
    path('' , views.deface , name='list'),
]