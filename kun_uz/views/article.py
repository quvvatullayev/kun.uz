from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from ..models import (
    Article,
    Article_piece,
    
)
from ..serialization import (
    ArticleSerializer,
    Article_pieceSerializer,
)

class CreateArticle(APIView):
    def post(self, request: Request):
        serializer = ArticleSerializer(data=request.data)
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
    
class GetArticle(APIView):
    def get(self, request: Request):
        article = Article.objects.all()
        print(article)
        serializer = ArticleSerializer(article, many=True)
        print(serializer.data)
        data = {'article': []}
        for i in serializer.data[-6:]:
            article_piece = Article_piece.objects.filter(article=i['id'])
            serializer2 = Article_pieceSerializer(article_piece, many=True)
            data['article'].append({
                'id': i['id'],
                'title': i['title'],
                'description': i['description'],
                'img': i['img'],
                "jurnalist": i['jurnalist'],
                'created': i['created'],
                'article_piece': serializer2.data
            })
        return Response(data, status=status.HTTP_200_OK)
    
class UpdateArticle(APIView):
    def post(self, request: Request, pk):
        article = Article.objects.get(id=pk)
        serializer = ArticleSerializer(instance=article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(
            {
                "message": "Error",
                "errors": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST)
    
class DeleteArticle(APIView):
    def post(self, request: Request, pk):
        article = Article.objects.get(id=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ArticleList(APIView):
    def get(self, request: Request):
        article = Article.objects.all()
        serializer = ArticleSerializer(article, many=True)
        data = {'article': []}
        for i in serializer.data:
            article_piece = Article_piece.objects.filter(article=i['id'])
            serializer2 = Article_pieceSerializer(article_piece, many=True)
            data['article'].append({
                'id': i['id'],
                'title': i['title'],
                'description': i['description'],
                'img': i['img'],
                'created': i['created'],
                'jurnalist': i['jurnalist'],
                'article_piece': serializer2.data,
            })
        return Response(data, status=status.HTTP_200_OK)
    
class ArticleDetail(APIView):
    def get(self, request: Request, pk):
        article = Article.objects.get(id=pk)
        serializer = ArticleSerializer(article)
        article_piece = Article_piece.objects.filter(article=pk)
        serializer2 = Article_pieceSerializer(article_piece, many=True)
        data = serializer.data
        data['article_piece'] = serializer2.data
        return Response(data, status=status.HTTP_200_OK)
    
