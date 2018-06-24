from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=50)
	def __str__(self):
		return self.name
	class Meta:
		verbose_name = "Categorie"

class Quiz(models.Model):
	category = models.ForeignKey(Category,on_delete=models.CASCADE)
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	description = models.TextField(max_length=1000)
	title = models.CharField(max_length=100)
	photo = models.ImageField(upload_to="quiz/photos")
	status = models.CharField(max_length=1,choices=(("1","Active"),("0","Inactive")))
	def __str__(self):
		return self.title

class Question(models.Model):
	quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)
	question = models.CharField(max_length=1000)
	points = models.IntegerField()
	def __str__(self):
		return ("#{}#{} - {}".format(self.quiz.id,self.id,self.question))

class Answer(models.Model):
	question = models.ForeignKey(Question,on_delete=models.CASCADE)
	answer = models.TextField(max_length=1000)
	correct = models.CharField(max_length=5,choices=(("0","Not correct"),("1","Correct")))
	def __str__(self):
		return ("#{}#{} - {}".format(self.question.id,self.id,self.answer))
