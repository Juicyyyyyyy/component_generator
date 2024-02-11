from django.shortcuts import render


def generate_component(request):
    return render(request, 'software/generate_component.html')
