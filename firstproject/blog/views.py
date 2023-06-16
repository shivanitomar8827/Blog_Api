from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


from rest_framework.decorators import api_view,APIView


from rest_framework.response import Response

from rest_framework import status

from .models import Blog
from blog.serializers import BlogSerializer




#function based views

# @api_view(['GET', 'POST'])
# def blog_list(request):
   
#     if request.method == 'GET':
#         blogs = Blog.objects.all()
#         serializer = BlogSerializer(blogs, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = BlogSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#class based views

class Blogpost(APIView):
   
    def get(self, request, format=None):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



#from.serializer import blogSerializer
# from rest_framework.generics import CreateAPIView
# from .serializers import blogSerializer

# class blog_listCreate(CreateAPIView):
#     queryset = blog.objects.all()
#     serializer_calss = blogSerializer
