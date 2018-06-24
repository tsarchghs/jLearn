from django.urls import path
from . import views

urlpatterns = [
	path("",views.redirectToHome,name="redirectToHome"),
	path("home",views.home,name="home"),
]	