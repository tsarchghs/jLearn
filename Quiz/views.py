from django.shortcuts import render

# Create your views here.

def showQuiz(request):
	return render(request,"showQuiz.html")
	