from django.urls import path
from . import views

urlpatterns = [
	path("quiz/<ID>",views.showQuiz,name="showQuiz"),	
]