from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Quiz.models import Category,Quiz #,Question,Answer
from django.contrib.auth import authenticate
from django.contrib.auth.views import login

# Create your views here.

def home(request):
	quizzes = Quiz.objects.all()
	for quiz in quizzes:
		if len(quiz.description) > 241:
			quiz.description = quiz.description[:237] + "..."
	context = {"quizzes":quizzes}
	if request.method == "POST":            
		username=request.POST.get("username")
		password = request.POST.get("password")                     
		user = authenticate(request, username=username, password=password)
		if user is not None:
			return login(request)
		else:
			return render(request,"home.html",{'invalid': True })
	else:
		return render(request,"home.html",context)
