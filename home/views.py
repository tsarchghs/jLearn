from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Quiz.models import Category,Quiz #,Question,Answer
from django.shortcuts import redirect
from authentication import views as auth_views
# Create your views here.

def home(request):
	quizzes = Quiz.objects.filter(status="1")
	for quiz in quizzes:
		if len(quiz.description) > 241:
			quiz.description = quiz.description[:237] + "..."
	context = {"quizzes":quizzes}
	if request.method == "POST":
		return auth_views.custom_login(request,context)
	else:
		return render(request,"home.html",context)

def redirectToHome(request):
	return redirect("/home")