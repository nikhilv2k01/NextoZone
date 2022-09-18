from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.parsers import JSONParser

# Create your views here.


# Register API
class RegisterView(APIView):
    def post(self, request):

        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data = [serializer.data]
            return Response({
                "status": True,
                "status_code": status.HTTP_200_OK,
                "discription": "register success",
                "data": data,
            })
        return Response(serializer.errors)


# Login API
class LoginView(APIView):
    def post(self, request):

        serializer_data = JSONParser().parse(request)
        serializer = LoginSerializer(data=serializer_data)
        password = serializer_data['password']
        user_name = serializer_data['user_name']

        if serializer.is_valid(raise_exception=True):
            if '@' in user_name:
                id = Register.objects.filter(
                    email_id=user_name, password=password).first()
            else:
                id = Register.objects.filter(
                    user_name=user_name, password=password).first()
            user_id = id.user_id
            user_name = id.user_name
            email_id = id.email_id
            phone = id.phone

            response = Response()
            response.data = {
                'status': True,
                'status_code': status.HTTP_200_OK,
                'description': 'login success',
                'data': [{
                    "user_id": user_id,
                    "user_name": user_name,
                    "email_id": email_id,
                    "phone": phone,
                }]
            }
            return response
        return Response(serializer.errors)
