# import json
# from http import HTTPStatus
#
# from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed
# from django.shortcuts import get_object_or_404
# from django.urls import reverse
# from django.views.decorators.csrf import csrf_exempt
#
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework import mixins, generics

from blog.models import Post
from blog.api.serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# @api_view(['GET', 'POST'])
# def post_list(request, format=None):
#     if request.method == 'GET':
#         posts = Post.objects.all()
#         # return JsonResponse({"data": PostSerializer(posts, many=True).data})
#         return Response({'data': PostSerializer(posts, many=True).data})
#     elif request.method == 'POST':
#         # post_data = json.loads(request.body)
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             post = serializer.save()
#             return HttpResponse(
#                 status=HTTPStatus.CREATED,
#                 headers={'Location': reverse('api_post_detail', args=(post.pk,))}
#             )
#         return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)
#
#


# class PostList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     # model = Post.objects.all()
#     serializer_class = PostSerializer
#
#     def get_queryset(self):
#         return Post.objects.all()
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# @api_view(['GET', 'PUT', 'DELETE'])
# def post_detail(request, pk, format=None):
#     try:
#         post = Post.objects.get(pk=pk)
#     except Post.DoesNotExist:
#         return Response(status=HTTPStatus.NOT_FOUND)
#
#     if request.method == 'GET':
#         return Response(PostSerializer(post).data)
#     elif request.method == 'PUT':
#         serializer = PostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return HttpResponse(status=HTTPStatus.NO_CONTENT)
#         return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)
#     elif request.method == 'DELETE':
#         post.delete()
#         return Response(status=HTTPStatus.NO_CONTENT)

# class PostDetail(
#     mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     generics.GenericAPIView,
# ):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# class PostDetail(APIView):
#     @staticmethod
#     def get_post(pk):
#         return get_object_or_404(Post, pk=pk)
#
#     def get(self, request, pk, format=None):
#         post = self.get_post(pk)
#         return Response(PostSerializer(post).data)
#
#     def put(self, request, pk, format=None):
#         post = self.get_post(pk)
#         serializer = PostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return HttpResponse(status=HTTPStatus.NO_CONTENT)
#         return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         post = self.get_post(pk)
#         post.delete()
#         return Response(status=HTTPStatus.NO_CONTENT)