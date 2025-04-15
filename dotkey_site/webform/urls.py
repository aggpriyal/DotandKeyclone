# webform/urls.py

from django.urls import path
from .views import home_view,contact_view, success_view

urlpatterns = [
    path('', home_view, name="home"),
    path('contact/', contact_view, name="contact"),
    path('success/', success_view, name="success"),
]
