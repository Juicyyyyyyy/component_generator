# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, LoginForm


def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['email']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']

            # Check if passwords match
            if password != password2:
                return render(request, 'register.html', {'form': form, 'error': 'Passwords do not match'})

            try:
                # Create a new user
                user = User.objects.create_user(username, email, password)

                user.first_name = first_name
                user.last_name = last_name
                user.save()
                # Log in the user immediately after registration
                login(request, user)

                # Redirect to the home page or a profile page
                return redirect('/')
            except Exception as e:
                # Handle user creation error
                print(f"Error creating user: {e}")
                return render(request, 'register.html', {'form': form, 'error': 'An error has occurred'})
        else:
            return render(request, 'register.html', {'form': form, 'error': 'The form is not valid. Please try again.'})

    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def logout_view(request):
    logout(request)  # Use the logout function provided by Django
    return redirect('/')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print(f"Email: {email}, Password: {password}")
            # Authenticate user
            user = authenticate(request, username=email, password=password)

            if user is not None:
                # Login the user
                login(request, user)

                # Redirect to the home page or a profile page
                return redirect('/')
            else:
                # Authentication failed, show error message
                return render(request, 'login.html', {'form': form, 'error': 'Invalid credentials'})
        else:
            return render(request, 'login.html', {'form': form, 'error': 'The form is not valid. Please try again.'})
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
