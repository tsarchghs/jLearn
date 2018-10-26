from django.urls import path
from . import views

urlpatterns = [
	path("create/<str:model_name>",views.create,name="create_api")
	#path("create_quiz",views.create_quiz,name="create_quiz_api"),
	#path("create_question",views.create_question,name="create_question_api"),
	#path("create_answer",views.create_answer,name="create_answer_api"),
]