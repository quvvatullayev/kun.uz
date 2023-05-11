from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from ..models import (
    Actual,
)
from ..serialization import (
    ActualSerializer,
)

class CreateActual(APIView):
    authentication_classes = [TokenAuthentication]
    def post(self, request: Request):
        serializer = ActualSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            {
                "message": "Error",
                "errors": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    
class GetActual(APIView):
    def get(self, request: Request):
        actual = Actual.objects.all()
        serializer = ActualSerializer(actual, many=True)
        return Response(serializer.data[-5:], status=status.HTTP_200_OK)
    
class UpdateActual(APIView):
    authentication_classes = [TokenAuthentication]
    def post(self, request: Request, pk):
        actual = Actual.objects.get(id=pk)
        serializer = ActualSerializer(instance=actual, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(
            {
                "message": "Error",
                "errors": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST)
    
class DeleteActual(APIView):
    authentication_classes = [TokenAuthentication]
    def post(self, request: Request, pk):
        actual = Actual.objects.get(id=pk)
        actual.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)