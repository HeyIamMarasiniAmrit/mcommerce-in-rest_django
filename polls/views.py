from django.shortcuts import render
from django.db.models import query
from .models import polls
from .serializers import pollsSerializer


from polls.views import ListPolls

from .serializers import pollsSerializer,MessageSerializer
from .import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .test import Message
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets

# Create your views here.

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])

def listPolls(request):
    query = polls.objects.all()

    serializer_class = pollsSerializer(query,many=True)
    context ={
        'serializer_class_data':serializer_class.data
    }
    return Response(serializer_class.data)

# creating get , post method

@api_view(['GET','POST'])
def listmessages(request):
    message_obj=Message('raja@python.com', 'hi how are you')
    serializer_class = MessageSerializer(message_obj)
    return Response(serializer_class.data)

class ListPolls(APIView):

   def get(self, request):
       query = polls.objects.all()
       serializer_class = pollsSerializer(query, many=True)


class productDetailsView(APIView):
    def get(self, request):
        query = polls.objects.all()
        serializer = pollsSerializer(query, many=True)
        return Response(serializer.data)


    def post(self,request):
        serializer_obj = productserializer(data = request.data)
        if serializer_obj.is_valid(raise_exception=True):
            product_saved=serializer_obj.save()
            return Response("Success":"Product '{}' created successfully".formate(product_saved.name))
        return Response(serializer_obj.errors, status=status.HTTP_200_ok)

    def put(self, request,pid):
        product_obj=Product.objects.get(product_id = pid)
        serializer_obj = productserializer(data=request.data)
        if serializer_obj.is_valid(raise_exception=True):
                product_saved = serializer_obj.save()
                return Response("Success":"Product '{}' updated successfully".formate(product_saved.name))
                return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pid):
        product_obj = product.objects.filter(product_id=pid).delete()
        return Response(serializer_obj.errors, status=status.HTTP_200_ok)
        

class listproductsMixins(mixins.listModelMixin,generics.GenericAPIView):
     queryset = Product.objects.all()
     serializer_class = ProductSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request,*args,**kwargs)

class DetailedProductMixins(mixins.RetrieveModelMixin,
                            mixins.CreateModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class ListProductGenerics(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = productSerializer

class DetailedProductGenerics(generics.RetrieveAPIView,
                              generics.UpdateAPIView,
                              generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = productSerializer

class SpecialProductGenerics(generics.ListCreateAPIView,
                              generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = productSerializer

class productviewset(viewsets.modelviewset):
    queryset = Product.objects.all()
    serializer_class = productSerializer
