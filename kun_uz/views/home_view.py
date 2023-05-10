from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from ..models import (
    New_type,
    Area,
    Day_new,
    Day_new_piece,
    Actual,
    Actual_piece,
    Intervyu,
    Intervyu_piece,
    Article,
    Article_piece,
    Bisnes_new,
    Bisnes_new_piece,
    Video_new,
    Video_new_piece,
)

from ..serialization import (
    New_typeSerializer,
    AreaSerializer,
    Day_newSerializer,
    Day_new_pieceSerializer,
    ActualSerializer,
    Actual_pieceSerializer,
    IntervyuSerializer,
    Intervyu_pieceSerializer,
    ArticleSerializer,
    Article_pieceSerializer,
    Bisnes_newSerializer,
    Bisnes_new_pieceSerializer,
    Video_newSerializer,
    Video_new_pieceSerializer,
)

class HomeView(APIView):
    def get(self, request: Request):
        new_type_list = New_type.objects.all()
        area_list = Area.objects.all()

        day_new_list = Day_new.objects.all()
        day_news = Day_newSerializer(day_new_list, many=True).data
        day_new_data = []
        for day_new in day_news[-5:]:
            day_new_piece_list = Day_new_piece.objects.filter(day_new=day_new['id'])
            day_new_data.append({
                'id': day_new['id'],
                'title': day_new['title'],
                'description': day_new['description'],
                'img': day_new['img'],
                'created': day_new['created'],
                'day_new_piece_list': Day_new_pieceSerializer(day_new_piece_list, many=True).data
            })
        
        actual_list = Actual.objects.all()
        actual_lists = ActualSerializer(actual_list, many=True).data
        actual_data = []
        for actual in actual_lists[-5:]:
            actual_piece_list = Actual_piece.objects.filter(actual=actual['id'])
            actual_data.append({
                'id': actual['id'],
                'title': actual['title'],
                'description': actual['description'],
                'img': actual['img'],
                'created': actual['created'],
                'actual_piece_list': Actual_pieceSerializer(actual_piece_list, many=True).data
            })

        intervyu_list = Intervyu.objects.all()
        intervyu_lists = IntervyuSerializer(intervyu_list, many=True).data
        intervyu_data = []
        for intervyu in intervyu_lists[-4:]:
            intervyu_piece_list = Intervyu_piece.objects.filter(intervyu=intervyu['id'])
            intervyu_data.append({
                'id': intervyu['id'],
                'title': intervyu['title'],
                'description': intervyu['description'],
                'img': intervyu['img'],
                'created': intervyu['created'],
                'intervyu_piece_list': Intervyu_pieceSerializer(intervyu_piece_list, many=True).data
            })

        article_list = Article.objects.all()
        article_lists = ArticleSerializer(article_list, many=True).data
        article_data = []
        for article in article_lists[-6:]:
            article_piece_list = Article_piece.objects.filter(article=article['id'])
            article_data.append({
                'id': article['id'],
                'title': article['title'],
                'description': article['description'],
                'img': article['img'],
                'created': article['created'],
                'article_piece_list': Article_pieceSerializer(article_piece_list, many=True).data
            })

        bisnes_new_list = Bisnes_new.objects.all()
        bisnes_new_data = []
        for bisnes_new in bisnes_new_list:
            bisnes_new = Bisnes_newSerializer(bisnes_new).data
            bisnes_new_piece_list = Bisnes_new_piece.objects.filter(bisnes_new=bisnes_new['id'])
            bisnes_new_data.append({
                'id': bisnes_new['id'],
                'title': bisnes_new['title'],
                'comment': bisnes_new['comment'],
                'description': bisnes_new['description'],
                'img': bisnes_new['img'],
                'created': bisnes_new['created'],
                'bisnes_new_piece_list': Bisnes_new_pieceSerializer(bisnes_new_piece_list, many=True).data
            })

        video_new_list = Video_new.objects.all()
        video_new_lists = Video_newSerializer(video_new_list, many=True).data
        video_new_data = []
        for video_new in video_new_lists[-6:]:
            video_new_piece_list = Video_new_piece.objects.filter(video_new=video_new['id'])
            video_new_data.append({
                'id': video_new['id'],
                'title': video_new['title'],
                'description': video_new['description'],
                'img': video_new['img'],
                'created': video_new['created'],
                'video_new_piece_list': Video_new_pieceSerializer(video_new_piece_list, many=True).data
            })
        

        return Response({
            'home': {
                'new_type_list': New_typeSerializer(new_type_list, many=True).data,
                'area_list': AreaSerializer(area_list, many=True).data,
                'day_new_list': day_new_data,
                'actual_list': actual_data,
                'intervyu_list': intervyu_data,
                'article_list': article_data,
                'bisnes_new_list': bisnes_new_data,
                'video_new_list': video_new_data,
            }}, status=status.HTTP_200_OK)