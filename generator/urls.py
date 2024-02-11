from django.urls import path
from . import views

urlpatterns = [
    path('generate-component', views.generate_component, name='generate-component'),
]
