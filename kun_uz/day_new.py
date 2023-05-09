from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from models import (
    Day_new,
)
from serialization import (
    Day_newSerializer,
)

class Create_day_new(APIView):
    def post(self, request):
        serializer = Day_newSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class List_day_new(APIView):
    def get(self, request:Request):
        day_new = Day_new.objects.all()[-5:]
        serializer = Day_newSerializer(day_new, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class Detail_day_new(APIView):
    def get(self, request:Request, pk):
        day_new = Day_new.objects.get(id=pk)
        serializer = Day_newSerializer(day_new)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class Update_day_new(APIView):
    def post(self, request:Request, pk):
        day_new = Day_new.objects.get(id=pk)
        serializer = Day_newSerializer(instance=day_new, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
class Delete_day_new(APIView):
    def delete(self, request:Request, pk):
        day_new = Day_new.objects.get(id=pk)
        day_new.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)