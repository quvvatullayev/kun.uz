from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class Register(APIView):
    def post(self, request: Request):
        username = request.data.get("username")
        password = request.data.get("password")
        if User.objects.filter(username=username):
            return Response(
                {
                    "message": "Error",
                    "errors": "Username already exists"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        if username is None or password is None:
            return Response(
                {
                    "message": "Error",
                    "errors": "Please provide both username and password"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        user = User.objects.create_user(username=username, password=password)
        token = Token.objects.create(user=user)
        return Response(
            {
                "message": "Success",
                "token": token.key
            },
            status=status.HTTP_201_CREATED
        )