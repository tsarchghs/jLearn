from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Quiz.models import Category,Quiz #,Question,Answer

# Create your views here.

def home(request):
	quizzes = Quiz.objects.all()
	for quiz in quizzes:
		if len(quiz.description) > 241:
			quiz.description = quiz.description[:237] + "..."
	context = {"quizzes":quizzes}
	return render(request,"home.html",context)
