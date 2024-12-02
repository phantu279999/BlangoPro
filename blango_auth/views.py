from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views import generic

from django_registration.backends.activation.views import RegistrationView
from .forms import BlangoRegistrationForm


class CustomRegistrationView(RegistrationView):
	form_class = BlangoRegistrationForm


@login_required
def profile(request):
	return render(request, 'blango_auth/profile.html')


class LogOutView(generic.RedirectView):
	url = reverse_lazy('index')

	def get(self, request, *args, **kwargs):
		logout(request)
		return super().get(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		logout(request)
		return super().post(request, *args, **kwargs)
