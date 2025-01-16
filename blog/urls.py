from django.urls import path, include

from . import views


urlpatterns = [
	path('', views.index, name='index'),
	path('ip/', views.get_ip, name='get_ip'),
	path('post/<slug>/', views.post_detail, name='blog-post-detail'),
	path('posts-tag/<int:pk>/', views.list_post_by_tag, name='posts-tag'),
	path('api/v1/', include('blog.api.urls'))
]
