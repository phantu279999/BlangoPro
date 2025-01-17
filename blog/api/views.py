from rest_framework import generics, permissions
from rest_framework.authentication import SessionAuthentication

from blog.models import Post
from blog.api.serializers import PostSerializer
from blog.api.permissions import AuthorModifyOrReadOnly, IsAdminUserForObject



class PostList(generics.ListCreateAPIView):
    authentication_classes = [AuthorModifyOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
