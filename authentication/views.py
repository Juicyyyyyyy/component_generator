# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm


def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']

            # Check if passwords match
            if password != password2:
                return render(request, 'register.html', {'form': form, 'error': 'Passwords do not match'})

            try:
                # Create a new user
                user = User.objects.create_user(username, email, password)
                print(f"User created: {user}")

                # Log in the user immediately after registration
                login(request, user)

                # Redirect to the home page or a profile page
                return redirect('/')
            except Exception as e:
                # Handle user creation error
                print(f"Error creating user: {e}")
                return render(request, 'register.html', {'form': form, 'error': 'Error creating user'})

    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def logout_view(request):
    logout(request)  # Use the logout function provided by Django
    return redirect('/')


def login_view(request):
    return render(request, 'login.html')
