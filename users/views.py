from django.shortcuts import render
from django.contrib.auth.views import login
from django.contrib.auth import authenticate, update_session_auth_hash
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

# Create your views here.

def custom_login(request,**kwargs):
	if request.user.is_authenticated:
		return redirect("/home")
	elif request.method == "POST":            
		username=request.POST.get("username")
		password = request.POST.get("password")                     
		user = authenticate(request, username=username, password=password)
		if user is not None:
			return login(request)
		else:
			return render(request,"registration/login.html",{'invalid': True })
	elif request.method == "GET":
		return login(request)

@login_required
def account(request):
	return render(request,"registration/showAccInfo.html")

@login_required
def editAccount(request,id):
	if request.method != "POST":
		return render(request,"registration/editAccInfo.html")
	else:
		_first_name = request.POST.get('first_name')
		_last_name = request.POST.get('last_name')
		_email = request.POST.get('email')
		_username = request.POST.get('username')
		#Removed a line here -------

		user = User.objects.get(pk=id)

		user.first_name = _first_name
		user.last_name = _last_name
		user.email = _email
		user.username = _username

		user.save()
		return redirect("/users/account")


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return render(request,"registration/change_password.html",{'form': form,"successful":True})
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {
        'form': form
    })