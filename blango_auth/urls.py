from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
	path("", include("django_registration.backends.activation.urls")),
	# path("", include("django.contrib.auth.urls")),
	# path("", include("allauth.urls")),
	path('login/', auth_views.LoginView.as_view(template_name='blango_auth/login.html'), name='login'),
	path('logout/', views.LogOutView.as_view(), name='logout'),
	path("profile/", views.profile, name="profile"),
	path(
		"register/",
		views.CustomRegistrationView.as_view(),
		name="django_registration_register",
	),
]