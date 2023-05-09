from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from ..models import (
    Area,
)
from ..serialization import (
    AreaSerializer,
)

class Create_area(APIView):
    def post(self, request):
        serializer = AreaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class List_area(APIView):
    def get(self, request:Request):
        area = Area.objects.all()
        serializer = AreaSerializer(area, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class Detail_area(APIView):
    def get(self, request:Request, pk):
        area = Area.objects.get(id=pk)
        serializer = AreaSerializer(area)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class Update_area(APIView):
    def post(self, request:Request, pk):
        area = Area.objects.get(id=pk)
        serializer = AreaSerializer(instance=area, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class Delete_area(APIView):
    def delete(self, request:Request, pk):
        area = Area.objects.get(id=pk)
        area.delete()
        return Response({'message': 'deleted'}, status=status.HTTP_200_OK)