from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import PostSerializer
from posts.models import Post
from rest_framework import generics, mixins


# class test_ApiView(APIView):
#     permission_classes = [IsAuthenticated]
#     def get(self, request, *args, **kwargs):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
        
#         return Response(serializer.data)
    
#     def post(self, request, *args, **kwargs):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
            
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
# abstracted into this:
# class GenericPostView(mixins.ListModelMixin,mixins.CreateModelMixin, generics.GenericAPIView):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()
    
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
# abstracted into this:

class GenericPostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    
class RetrieveDeleteUpdatePostView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()