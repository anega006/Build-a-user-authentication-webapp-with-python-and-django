from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .forms import SignUpForm, EditProfileForm, EditPasswordForm

# Create your views here.

def index(request):
	return render(request, 'User_Authentication_WebApp/index.html', {})


def login_user(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, ('You have been successfully logged in!'))
			# Redirect to a success page.   
			return redirect('index')
		else:
			# Return an 'invalid login' error message.
			messages.warning(request, ('Error logging in! Please try again...'))
			return redirect('login')
	else:
		return render(request, 'User_Authentication_WebApp/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out!'))
    # Redirect to a success page
    return redirect('index')


def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(request, username=username, password=password)
			login(request, user)
			messages.success(request, ('You have been successfully registered!'))
			return redirect('index')
	else:
		form = SignUpForm()
	
	context = {'form': form}
	return render(request, 'User_Authentication_WebApp/register.html', context)


def edit_profile(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			messages.success(request, ('Changes applied successfully to your profile!'))
			return redirect('index')
	else:
		form = EditProfileForm(instance=request.user)
	
	context = {'form': form}
	return render(request, 'User_Authentication_WebApp/edit_profile.html', context)


def change_password(request):
	if request.method == 'POST':
		form = EditPasswordForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			messages.success(request, ('Password updated successfully!'))
			return redirect('index')
	else:
		form = EditPasswordForm(user=request.user)
	
	context = {'form': form}
	return render(request, 'User_Authentication_WebApp/change_password.html', context)
