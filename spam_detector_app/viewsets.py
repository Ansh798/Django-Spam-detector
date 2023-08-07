from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer,ContactsSerializer
from .models import Users,Contacts


@api_view(['POST'])
def create_user(request):
   try:
      if request.method == "POST":
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"User created successfully"},status=200)
        return Response(serializer.errors,status=400)
   except Exception as e:
      return Response(str(e),status=400)

@api_view(['GET'])
def get_profile(request):
    try:
      if request.method == 'GET':
        phone = int(request.query_params.get('phone'))
        user = Users.objects.filter(phone=phone).values("name","phone","is_spam")
        if user  :
            res=user
        else:
            contact = Contacts.objects.filter(phone=phone).values("name","phone","is_spam")
            if contact :
                res=contact
            else:
                return Response({"message":"Phone number doest not exist"})
        result={
           "User":res
        }
        return Response(result,status=200)
    except Exception as e:
        return Response(str(e),status=400)
      
@api_view(['POST'])
def spam(request):
    try:
       if request.method == "POST":
          phone_number=int(request.data.get("phone"))
        #   import pdb;pdb.set_trace()
          user = Users.objects.filter(phone=phone_number).first()
          if user:
            if user.is_spam==False:
                user.is_spam=True
                user.save()
                return Response({"message":"Marked as spam"},status=200)     
            elif user.is_spam ==True:  
                user.is_spam=False
                user.save()
                return Response({"message":"Removed as spam"},status=200)
          else :
             contact=Contacts.objects.get(phone=phone_number)
             if contact.is_spam == False:
                contact.is_spam=True
                contact.save()
                return Response({"message":"CMarked as spam"},status=200)     
             elif contact.is_spam==True:  
                contact.is_spam=False
                contact.save()
                return Response({"message":"CRemoved as spam"},status=200)
              
    except Exception as e:
        return Response(str(e),status=400)