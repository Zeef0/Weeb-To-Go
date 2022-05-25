from django.contrib import admin
from django.urls import path

from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='anime/home.html'), name="home"),
]
