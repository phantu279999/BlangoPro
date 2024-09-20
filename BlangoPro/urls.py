from django.contrib import admin
from django.urls import path, include
from django.conf import settings
import debug_toolbar
import blog.views

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', blog.views.index),
	path('ip/', blog.views.get_ip),
	path('post/<slug>/', blog.views.post_detail, name='blog-post-detail')
]


if settings.DEBUG:
	urlpatterns += [
		path("__debug__/", include(debug_toolbar.urls)),
	]