from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="MEMESHACK"),
    path('rickroll', views.rickroll, name="rickrolled"),
]
