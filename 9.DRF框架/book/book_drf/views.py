from rest_framework.views import APIView
from django.http import JsonResponse
from book_manage.models import BookInfo
from .serializer import BookSerialzier
from rest_framework.generics import (ListAPIView,
                                     CreateAPIView,
                                     UpdateAPIView,
                                     RetrieveAPIView,
                                     DestroyAPIView)

# Create your views here.

class Books(APIView):

    def get(self,request):
        # 1、查询所有图书对象
        books = BookInfo.objects.all()
        ser=BookSerialzier(books,many=True)
        print(ser, '=========================ser')
        return JsonResponse(ser.data, safe=False)


class Book(APIView):

    def get(self,request):
        book=BookInfo.objects.get(id=1)
        ser = BookSerialzier(book)

        return JsonResponse(ser.data)

