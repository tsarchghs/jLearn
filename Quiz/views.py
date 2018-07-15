from django.shortcuts import render
from .models import *
# Create your views here.

def getQuestion_answers(ID):
	quiz = Quiz.objects.get(pk=ID)
	question_answers = {}
	questions = Question.objects.filter(quiz=quiz)
	answers = Answer.objects.filter(question__in=questions)
	for question in questions:
		q_answers = Answer.objects.filter(question=question)
		question_answers[question] = q_answers
	return question_answers

def showQuiz(request,ID):
	quiz = Quiz.objects.get(pk=ID)
	question_answers = getQuestion_answers(ID)
	context = {"quiz":quiz,"question_answers":question_answers}
	return render(request,"showQuiz.html",context)

def submitQuiz	(request,ID):
	quiz = Quiz.objects.get(pk=ID)
	if request.method == "POST":
		pass

