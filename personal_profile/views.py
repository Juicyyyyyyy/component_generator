from django.shortcuts import render, redirect
from generator.models import Component


def profile(request):
    if request.user.is_authenticated:
        user_components = Component.objects.filter(project_id__owner_id=request.user).order_by('-id')
        return render(request, 'profile.html', {'user_components': user_components})
    else:
        # Redirect to login if the user is not authenticated
        return redirect('login')
