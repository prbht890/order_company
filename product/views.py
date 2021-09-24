from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from django.core import serializers
from .models import Product
from .serializers import *
# Create your views here.

class ProductView(GenericAPIView):
    serializer_class = ProductSerializer
    def get(self,request):
        queryset = Product.objects.all()
        serializer = self.serializer_class(queryset,many=True)
        data = serializer.data
        product_data = {'data':data}
        return Response(product_data)


class ProductCreate(GenericAPIView):
    serializer_class = ProductSerializer
    def post(self, request):

        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product = serializer.save()
            return Response("successfully added")
                

class OrderClass(GenericAPIView):
    def get(self,request):
        return render(request,"index.html",)
