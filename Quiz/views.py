from django.shortcuts import render
from .models import *
# Create your views here.

def showQuiz(request,ID):
	quiz = Quiz.objects.get(pk=ID)
	question_answers = {}
	questions = Question.objects.filter(quiz=quiz)
	answers = Answer.objects.filter(question__in=questions)
	for question in questions:
		q_answers = Answer.objects.filter(question=question)
		question_answers[question] = q_answers
	context = {"quiz":quiz,"question_answers":question_answers}
	return render(request,"showQuiz.html",context)
