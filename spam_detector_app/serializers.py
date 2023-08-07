from rest_framework import serializers
from .models import Users,Contacts

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= Users
        fields= "__all__"


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Contacts
        fields= "__all__"
