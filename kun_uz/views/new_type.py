from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from ..models import (
    New_type,
)

from ..serialization import (
    New_typeSerializer,
)

class Create_new_type(APIView):
    authentication_classes = [TokenAuthentication]
    def post(self, request):
        serializer = New_typeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class List_new_type(APIView):
    def get(self, request:Request):
        new_type = New_type.objects.all()
        serializer = New_typeSerializer(new_type, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class Detail_new_type(APIView):
    def get(self, request:Request, pk):
        new_type = New_type.objects.get(id=pk)
        serializer = New_typeSerializer(new_type)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class Update_new_type(APIView):
    authentication_classes = [TokenAuthentication]
    def post(self, request:Request, pk):
        new_type = New_type.objects.get(id=pk)
        serializer = New_typeSerializer(instance=new_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class Delete_new_type(APIView):
    authentication_classes = [TokenAuthentication]
    def delete(self, request:Request, pk):
        new_type = New_type.objects.get(id=pk)
        new_type.delete()
        return Response({'message': 'deleted'}, status=status.HTTP_200_OK)
    