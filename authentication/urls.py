from django.urls import path
import django.contrib.auth.views as auth_views 

urlpatterns = [
	path("logout/",auth_views.logout,name="logout"),
]