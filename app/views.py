from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Identity
from .serializers import IdentitySerializer
from rest_framework.generics import CreateAPIView
from django.db.models import Q
# Create your views here.
class CreateIdentifyView(CreateAPIView):
    queryset = Identity.objects.all()
    serializer_class = IdentitySerializer


class GetIdentifyView(APIView):
    def post(self,request):
        email = request.data['email']
        phonenumber = request.data['phoneNumber']
        query = Identity.objects.filter(Q(email=email) | Q(phoneNumber=phonenumber))
        serializer = IdentitySerializer(query,many=True)
        data = serializer.data[0]
        if email == data['email'] and phonenumber == data['phoneNumber']:
            return Response(serializer.data)
        else:
            query = Identity.objects.filter(Q(email=email) | Q(phoneNumber=phonenumber)).values()[0]
            create_secondary = Identity(email=email,phoneNumber=phonenumber,linkedID=query['id'],linkprecedence='secondary')
            create_secondary.save()
            query = Identity.objects.filter(Q(email=email) | Q(phoneNumber=phonenumber))
            serializer = IdentitySerializer(query, many=True)
            return Response(serializer.data)


class IdentifyView(APIView):
    def post(self,request):
        email = request.data['email']
        phonenumber = request.data['phoneNumber']
        query = Identity.objects.filter(Q(email=email) | Q(phoneNumber=phonenumber)).values()
        temp  = {
            "contact" :{
                "primaryContactId":query[0]['id'],
                "emails":[data['email'] for data in query],
                "phone":list(set([data['phoneNumber']for data in query])),
                "secondaryContactIds":[data['id'] for data in query[1::]]
            }
        }
        return Response(temp)
