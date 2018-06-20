from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path("login/", views.custom_login,name="login"),
	path("logout/", auth_views.logout,{'next_page': '/users/login'},name="logout"),
	path("password_reset/", auth_views.password_reset,name="password_reset"),
	path("password_reset_done/", auth_views.password_reset_done,name="password_reset_done"),
	path('password_reset/<uidb64>-<token>', auth_views.password_reset_confirm, name='password_reset_confirm'),
    path('password_reset/done/', auth_views.password_reset_complete, name='password_reset_complete'),
	path("account/", views.account,name="account"),
	path("account/edit/<id>", views.editAccount,name="editAccount"),
	path("account/change_password", views.change_password,name="change_password"),
]