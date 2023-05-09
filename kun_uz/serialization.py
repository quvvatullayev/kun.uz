from rest_framework import serializers

from .models import (
    New_type,
    Area,
    Day_new,
    Day_new_piece,
    Actual,
    Actual_piece,
    Intervyu,
    Intervyu_piece,
    Article,
    Bisnes_new,
    Bisnes_new_piece,
    Video_new, 
    Video_new_piece,
    Area_new,
    Area_new_piece,
    Area_new_list,
    Area_new_list_piece,
)

class New_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = New_type
        fields = '__all__'

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'

class Actual_pieceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actual_piece
        fields = '__all__'

class Day_new_pieceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Day_new_piece
        fields = '__all__'

class Day_newSerializer(serializers.ModelSerializer):
    class Meta:
        model = Day_new
        fields = '__all__'

class ActualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actual
        fields = '__all__'



class IntervyuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intervyu
        fields = '__all__'

class Intervyu_pieceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intervyu_piece
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class Bisnes_newSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bisnes_new
        fields = '__all__'

class Bisnes_new_pieceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bisnes_new_piece
        fields = '__all__'

class Video_newSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video_new
        fields = '__all__'

class Video_new_pieceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video_new_piece
        fields = '__all__'
        
class Area_newSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area_new
        fields = '__all__'

class Area_new_pieceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area_new_piece
        fields = '__all__'

class Area_new_listSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area_new_list
        fields = '__all__'

class Area_new_list_pieceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area_new_list_piece
        fields = '__all__'