from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from rest_framework.decorators import APIView
from .models import Post
from .serializers import PostSerializer

posts = [
    {
        "id" : 1,
        "title" : "Why is it difficult to learn DRF?",
        "content" : "The reason is that it is framework"
    },
    {
        "id" : 2,
        "title" : "Why is it difficult to learn DRF? ..",
        "content" : "The reason is that it is framework"
    },
    {
        "id" : 3,
        "title" : "Why is it difficult to learn DRF? Answer",
        "content" : "The reason is that it is framework"
    },
],

class PostView(APIView):
    def get(self,request):
        response = Post.objects.all()
        serializer = PostSerializer(instance=response,many=True)
        return Response(serializer.data,status.HTTP_201_CREATED)
    
    def post(self,request):
        data = request.data
        serializer = PostSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {"Message":"success"}

            return Response(data=response,status=status.HTTP_202_ACCEPTED)
        
class PostRetrieveView(generics.GenericAPIView,mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)
    
    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)
    
    def put(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs)

