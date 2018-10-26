from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from Quiz.models import Quiz,Question,Answer

class QuizSerializer(serializers.ModelSerializer):
	class Meta:
		model = Quiz
		exclude = []

class QuizViewSet(viewsets.ModelViewSet):
	queryset = Quiz.objects.all()
	serializer_class = QuizSerializer

class QuestionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Question
		exclude = []

class QuestionViewSet(viewsets.ModelViewSet):
	queryset = Question.objects.all()
	serializer_class = QuestionSerializer

class AnswerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Answer
		exclude = []

class AnswerViewSet(viewsets.ModelViewSet):
	queryset = Answer.objects.all()
	serializer_class = AnswerSerializer


router = routers.DefaultRouter()
router.register(r'quizzes',QuizViewSet)
router.register(r'questions',QuestionViewSet)
router.register(r'answers',AnswerViewSet)

urlpatterns = [
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	path("",include(router.urls)),
]