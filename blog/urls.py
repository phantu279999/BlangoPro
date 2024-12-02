from django.urls import path

from . import views


urlpatterns = [
	path('', views.index, name='index'),
	path('ip/', views.get_ip, name='get_ip'),
	path('post/<slug>/', views.post_detail, name='blog-post-detail'),
]
