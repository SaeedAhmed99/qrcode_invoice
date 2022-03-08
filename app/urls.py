from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('pdfconv/', views.pdfreport, name='report'),
    path('qr/', views.qr)
]
