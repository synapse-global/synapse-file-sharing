from django.urls import path
from . import views

urlpatterns = [
    path('<str:key>/', views.get_file, name='get_file'),
]
