from django import forms
from .models import Quiz,Question,Answer

class QuizForm(forms.ModelForm):
	class Meta:
		model = Quiz
		exclude = []

class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		exclude = []

class AnswerForm(forms.ModelForm):
	class Meta:
		model = Answer
		exclude = []