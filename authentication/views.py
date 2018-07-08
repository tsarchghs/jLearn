from django.shortcuts import render
from django.contrib.auth.views import login
from django.contrib.auth import authenticate

# Create your views here.

def custom_login(request,context):
	username=request.POST.get("username")
	password = request.POST.get("password")                     
	user = authenticate(request, username=username, password=password)
	if user is not None:
		return login(request)
	else:
		context["invalid"] = True
		return render(request,"home.html",context)