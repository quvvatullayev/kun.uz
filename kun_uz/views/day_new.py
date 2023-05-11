from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from ..models import (
    Day_new,
    Day_new_piece,
)
from ..serialization import (
    Day_newSerializer,
    Day_new_pieceSerializer,
)

class Create_day_new(APIView):
    authentication_classes = [TokenAuthentication]
    def post(self, request):
        serializer = Day_newSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class List_day_new(APIView):
    def get(self, request:Request):
        day_new = Day_new.objects.all()
        serializer = Day_newSerializer(day_new, many=True)
        data = {'day_naws': []}
        n = 0
        for i in serializer.data:
            day_new_piece = Day_new_piece.objects.filter(day_new=i['id'])
            serializer_piece = Day_new_pieceSerializer(day_new_piece, many=True)
            data['day_naws'].append({
                'id': i['id'],
                'title': i['title'],
                'description': i['description'],
                'comment': i['comment'],
                'created': i['created'],
                'img': i['img'],
                'day_new_piece': serializer_piece.data,

            })

        return Response(data, status=status.HTTP_200_OK)
    
class Detail_day_new(APIView):
    def get(self, request:Request, pk):
        day_new = Day_new.objects.get(id=pk)
        day_new_piece = Day_new_piece.objects.filter(day_new=day_new)
        serializer_piece = Day_new_pieceSerializer(day_new_piece, many=True)
        serializer = Day_newSerializer(day_new)
        data = serializer.data
        data['day_new_piece'] = serializer_piece.data
        return Response(data, status=status.HTTP_200_OK)
    
class Update_day_new(APIView):
    authentication_classes = [TokenAuthentication]
    def post(self, request:Request, pk):
        day_new = Day_new.objects.get(id=pk)
        serializer = Day_newSerializer(instance=day_new, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
class Delete_day_new(APIView):
    authentication_classes = [TokenAuthentication]
    def delete(self, request:Request, pk):
        day_new = Day_new.objects.get(id=pk)
        day_new.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)