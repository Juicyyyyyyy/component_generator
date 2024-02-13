from django.urls import path
from . import views

urlpatterns = [
    path('software/generate_component/', views.generate_component, name='generate_component'),
]
