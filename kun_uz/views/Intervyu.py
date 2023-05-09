from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from ..models import (
    Intervyu,
)
from ..serialization import (
    IntervyuSerializer,
)

class CreateIntervyu(APIView):
    def post(self, request: Request):
        serializer = IntervyuSerializer(data=request.data)
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
    
class GetIntervyu(APIView):
    def get(self, request: Request):
        intervyu = Intervyu.objects.all()
        serializer = IntervyuSerializer(intervyu, many=True)
        return Response(serializer.data[-4:], status=status.HTTP_200_OK)
    
class IntervyuList(APIView):
    def get(self, request: Request):
        intervyu = Intervyu.objects.all()
        serializer = IntervyuSerializer(intervyu, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class UpdateIntervyu(APIView):
    def post(self, request: Request, pk):
        intervyu = Intervyu.objects.get(id=pk)
        serializer = IntervyuSerializer(instance=intervyu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(
            {
                "message": "Error",
                "errors": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST)
    
class DeleteIntervyu(APIView):
    def post(self, request: Request, pk):
        intervyu = Intervyu.objects.get(id=pk)
        intervyu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)