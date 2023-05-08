from rest_framework import serializers

from .models import (
    New_type,
    Area,
    Day_new,
    Actual,
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

class Day_newSerializer(serializers.ModelSerializer):
    class Meta:
        model = Day_new
        fields = '__all__'