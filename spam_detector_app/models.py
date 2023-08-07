from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Users(models.Model):
    name=models.CharField(max_length=50,null=False)
    phone=models.IntegerField(unique=True,null=False)
    email=models.EmailField(null=False)
    is_spam=models.BooleanField(default=False)
    def __str__(self):
          return self.name
    
class Contacts(models.Model):
    name=models.CharField(max_length=50,null=False)
    phone=models.IntegerField(null=False)
    contact=models.ForeignKey(Users,on_delete=models.CASCADE,null=False)
    is_spam=models.BooleanField(default=False)
    def __str__(self):
        return str(self.contact)

