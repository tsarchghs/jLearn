from django.shortcuts import render
from .models import *
# Create your views here.

def showQuiz(request,ID):
	quiz = Quiz.objects.get(pk=ID)
	context = {"quiz":quiz}
	return render(request,"showQuiz.html",context)
