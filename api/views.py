from django.shortcuts import render, HttpResponse,reverse
from django.http import Http404
from Quiz.models import Quiz
from Quiz.forms import QuizForm,QuestionForm,AnswerForm
import json
from jLearn.settings import DEBUG
# Create your views here.

def create(request,model_name):
	api_type = "create_{}".format(model_name)
	if model_name == "quiz":
		modelForm = QuizForm
	elif model_name == "question":
		modelForm = QuestionForm
	elif model_name == "answer":
		modelForm = AnswerForm
	if request.method == "POST":
		if model_name == "quiz":
			form = modelForm(request.POST,request.FILES)
		else:
			form = modelForm(request.POST)
		if form.is_valid():
			form.save()
			data = {"type":api_type,"successful":True,"errors":form.errors}
		else:
			data = {"type":api_type,"successful":False,"errors":form.errors}
		return HttpResponse(json.dumps(data),content_type="application/json")
	if DEBUG:
		form = modelForm()
		return render(request,"api/show_form.html",{"form":form})
	else:
		data = {"type":api_type,"successful":False,"error_message":"POST only"}	
		return HttpResponse(json.dumps(data),content_type="application/json")


"""
def create_quiz(request):
	if request.method == "POST":
		form = QuizForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			data = {"type":"create_quiz","successful":True,"errors":form.errors}
		else:
			data = {"type":"create_quiz","successful":False,"errors":form.errors}
		return HttpResponse(json.dumps(data),content_type="application/json")
	if DEBUG:
		form = QuizForm()
		return render(request,"api/show_form.html",{"form":form})
	else:
		data = {"type":"create_quiz","successful":False,"error_message":"POST only"}	
		return HttpResponse(json.dumps(data),content_type="application/json")


def create_question(request):
	if request.method == "POST":
		form = QuestionForm(request.POST)
		if form.is_valid():
			form.save()
			data = {"type":"create_question","successful":True,"errors":form.errors}
		else:
			data = {"type":"create_question","successful":False,"errors":form.errors}
		return HttpResponse(json.dumps(data),content_type="application/json")
	if DEBUG:
		form = QuestionForm()
		return render(request,"api/show_form.html",{"form":form})
	else:
		data = {"type":"create_question","successful":False,"error_message":"POST only"}	
		return HttpResponse(json.dumps(data),content_type="application/json")

def create_answer(request):
	if request.method == "POST":
		form = AnswerForm(request.POST)
		if form.is_valid():
			form.save()
			data = {"type":"create_answer","successful":True,"errors":form.errors}
		else:
			data = {"type":"create_answer","successful":False,"errors":form.errors}
		return HttpResponse(json.dumps(data),content_type="application/json")
	if DEBUG:
		form = AnswerForm()
		return render(request,"api/show_form.html",{"form":form})
	else:
		data = {"type":"create_answer","successful":False,"error_message":"POST only"}	
		return HttpResponse(json.dumps(data),content_type="application/json")"""