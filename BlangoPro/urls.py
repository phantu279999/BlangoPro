from django.contrib import admin
from django.urls import path, include
from django.conf import settings
import debug_toolbar


urlpatterns = [
	path('', include('blog.urls')),
	path('admin/', admin.site.urls),
	path("accounts/", include("blango_auth.urls")),
]

if settings.DEBUG:
	urlpatterns += [
		path("__debug__/", include(debug_toolbar.urls)),
	]
