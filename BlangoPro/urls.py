from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.auth import views as auth_views
import debug_toolbar
from django_registration.backends.activation.views import RegistrationView
from blango_auth.forms import BlangoRegistrationForm
import blog.views
import blango_auth.views

urlpatterns = [
	path('admin/', admin.site.urls),
	path('accounts/login/', auth_views.LoginView.as_view(template_name='blango_auth/login.html'), name='login'),
	# path("accounts/", include("django.contrib.auth.urls")),
	# path("accounts/", include("django_registration.backends.activation.urls")),
	# path(
	# 	"accounts/register/",
	# 	RegistrationView.as_view(form_class=BlangoRegistrationForm),
	# 	name="django_registration_register",
	# ),
	path('', blog.views.index),
	path('ip/', blog.views.get_ip),
	path('post/<slug>/', blog.views.post_detail, name='blog-post-detail'),
	path("accounts/profile/", blango_auth.views.profile, name="profile"),
	path("accounts/", include("allauth.urls")),
]

if settings.DEBUG:
	urlpatterns += [
		path("__debug__/", include(debug_toolbar.urls)),
	]
