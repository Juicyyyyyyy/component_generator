from django.shortcuts import render
from .models import Project, Component, Parameter, ParameterOption


def generate_component(request):
    parameters = Parameter.objects.all()
    parameter_options = ParameterOption.objects.all()
    return render(request, 'software/generate_component.html', {'parameters': parameters,
                                                                'parameter_options': parameter_options})
