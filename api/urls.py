from django import urls
from django.urls import path
from . import views

urlpatterns = [
    path('', views.BioView.as_view(), name="bio"),
    path('api/', views.OutputView.as_view(), name="calculate"),
]