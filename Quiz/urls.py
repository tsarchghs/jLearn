from django.urls import path
from . import views

urlpatterns = [
	path("quiz",views.showQuiz,name="showQuiz"),	
]