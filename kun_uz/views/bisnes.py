from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ..models import (
    Bisnes_new,
    Bisnes_new_piece,
)

from ..serialization import (
    Bisnes_newSerializer,
    Bisnes_new_pieceSerializer,
)

class CreateBisnes_new(APIView):
    def post(self, request: Request):
        serializer = Bisnes_newSerializer(data=request.data)
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
    
class Bisnes_newList(APIView):
    def get(self, request: Request):
        bisnes_new = Bisnes_new.objects.all()
        serializer = Bisnes_newSerializer(bisnes_new, many=True)
        data = {'bisnes_new': []}
        for i in serializer.data:
            bisnes_new_piece = Bisnes_new_piece.objects.filter(bisnes_new=i['id'])
            bisnes_new_piece_serializer = Bisnes_new_pieceSerializer(bisnes_new_piece, many=True)
            data['bisnes_new'].append({
                'id': i['id'],
                'title': i['title'],
                'description': i['description'],
                'img': i['img'],
                'created': i['created'],
                'bisnes_new_piece': bisnes_new_piece_serializer.data
            })

        return Response(data, status=status.HTTP_200_OK)
    
class UpdateBisnes_new(APIView):
    def post(self, request: Request, pk):
        bisnes_new = Bisnes_new.objects.get(id=pk)
        serializer = Bisnes_newSerializer(instance=bisnes_new, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(
            {
                "message": "Error",
                "errors": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    
class DeleteBisnes_new(APIView):
    def delete(self, request: Request, pk):
        bisnes_new = Bisnes_new.objects.get(id=pk)
        bisnes_new.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class DetailBisnes_new(APIView):
    def get(self, request: Request, pk):
        bisnes_new = Bisnes_new.objects.get(id=pk)
        serializer = Bisnes_newSerializer(bisnes_new)
        data = serializer.data
        bisnes_new_piece = Bisnes_new_piece.objects.filter(bisnes_new=pk)
        bisnes_new_piece_serializer = Bisnes_new_pieceSerializer(bisnes_new_piece, many=True)
        data['bisnes_new_piece'] = bisnes_new_piece_serializer.data
        return Response(data, status=status.HTTP_200_OK)