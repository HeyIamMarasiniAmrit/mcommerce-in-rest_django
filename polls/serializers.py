from rest_framework import serializers
from .models import polls


class pollsSerializer(serializers.ModelSerializer):
    class Meta:
       model = polls
       # fields = '__all__'
       fields= ['pr_id', 'name']

#simple serializer
class MessageSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.passwordField()
    content = serializers.CharField(max_length=260)
    created = serializers.DateTimeField()
