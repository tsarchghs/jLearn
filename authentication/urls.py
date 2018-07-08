from django.urls import path
import django.contrib.auth.views as auth_views 
from . import views
urlpatterns = [
	path("signup/",views.signup,name="signup"),
	path("logout/",auth_views.logout,name="logout"),
]