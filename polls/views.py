from django.shortcuts import render
from django.db.models import query
from .models import polls

from .serializers import pollsSerializer,MessageSerializer
from .import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .test import Message
from rest_framework.views import APIView
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
        query = product.objects.all()
        s
