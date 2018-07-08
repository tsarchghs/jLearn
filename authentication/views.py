from django.shortcuts import render, redirect
from django.contrib.auth.views import login
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def custom_login(request,template,context):
	username=request.POST.get("username")
	password = request.POST.get("password")                     
	user = authenticate(request, username=username, password=password)
	if user is not None:
		return login(request)
	else:
		context["invalid"] = True
		return render(request,template,context)

def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			return render(request, 'auth/signup.html', {'form': form,"successfully":True})
		else:
			return render(request, 'auth/signup.html', {'form': form})
	else:
		form = UserCreationForm()
		return render(request, 'auth/signup.html', {'form': form})
