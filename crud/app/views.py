from django.shortcuts import render
from rest_framework.views import APIView
from .models import Book
from .serializer import BookSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

class BookListCreateApiView(APIView):
    
    def get(self,request):
        
        books = Book.objects.all()
        serializer = BookSerializer(books,many=True)
        return Response (serializer.data,status=status.HTTP_200_OK)
    
    
    def post(self,request):
        
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    


class BookDetailApiView(APIView):
    
    def get(self,request,pk):
       
       if pk is not None: 
         obj = Book.objects.get(pk=pk)
         serializer = BookSerializer(obj)
         return Response(serializer.data,status=status.HTTP_200_OK)
         
       else:
           return Response("Book Not Exists !",status=status.HTTP_404_NOT_FOUND) 
       
       
        
        
    def put(self,request,pk):
        
        obj = get_object_or_404(Book,pk=pk)
      
        serializer = BookSerializer(obj,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        else:
            
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self,request,pk):
        
        book = get_object_or_404(pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        
            
        
      


