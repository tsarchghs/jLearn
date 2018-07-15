from django.shortcuts import render,redirect
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

def submitQuiz(request,ID):
	quiz = Quiz.objects.get(pk=ID)
	if request.method == "POST":
		correctAnswers = 0
		question_answers = getQuestion_answers(ID)
		user_question_answers = {}
		for question in question_answers:
			user_answers = request.POST.getlist(question.question)
			user_question_answers[question] = user_answers
		for question,answers in user_question_answers.items():
			if not 0 in answers:
				user_correct_answers = len(answers)
				current_question_correct_answers = 0
				current_question_answers = question_answers[question]
				for answer in current_question_answers:
					if answer.correct == "1":
						current_question_correct_answers += 1
				if user_correct_answers == current_question_correct_answers:
					correctAnswers += 1
				

		allQuestions = len(question_answers)
		context = {"correctAnswers":correctAnswers,"allQuestions":allQuestions}
		return render(request,"submitQuiz.html",context)
	else:
		return redirect("/quiz/{}".format(ID))

