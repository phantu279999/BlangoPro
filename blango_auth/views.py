from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views import generic


from django_registration.backends.activation.views import RegistrationView
from .forms import BlangoRegistrationForm
from blog.forms import AuthorProfileForm
from blog.models import AuthorProfile


class CustomRegistrationView(RegistrationView):
	form_class = BlangoRegistrationForm


@login_required
def profile(request):
	try:
		profile = AuthorProfile.objects.get(user_id=request.user.id)
	except AuthorProfile.DoesNotExist:
		AuthorProfile.objects.create(user=request.user, bio='').save()
		profile = AuthorProfile.objects.get(user_id=request.user.id)
	if request.method == 'POST':
		form = AuthorProfileForm(request.POST, instance=profile)
		if form.is_valid():
			form.save()
	else:
		form = AuthorProfileForm(instance=profile)
	return render(request, 'blango_auth/profile.html', {'profile': profile, 'form': form})


class LogOutView(generic.RedirectView):
	url = reverse_lazy('index')

	def get(self, request, *args, **kwargs):
		logout(request)
		return super().get(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		logout(request)
		return super().post(request, *args, **kwargs)
