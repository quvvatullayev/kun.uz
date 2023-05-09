from django.contrib import admin

from .models import (
    Area,
    Day_new,
    New_type,
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

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    

@admin.register(Day_new)
class Day_newAdmin(admin.ModelAdmin):
    list_display = ('title', 'comment', 'description', 'created',)
    list_filter = ('title', 'comment', 'description', 'created',)
    search_fields = ('title', 'comment', 'description', 'created',)
    ordering = ('title', 'comment', 'description', 'created',)
    

@admin.register(New_type)
class New_typeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    

@admin.register(Actual)
class ActualAdmin(admin.ModelAdmin):
    list_display = ('title', 'comment', 'description', 'created', 'author',)
    list_filter = ('title', 'comment', 'description', 'created', 'author',)
    search_fields = ('title', 'comment', 'description', 'created', 'author',)
    ordering = ('title', 'comment', 'description', 'created', 'author',)
    

@admin.register(Intervyu)
class IntervyuAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created', 'youtube_link', 'talked', 'painter',)
    list_filter = ('title', 'description', 'created', 'youtube_link', 'talked', 'painter',)
    search_fields = ('title', 'description', 'created', 'youtube_link', 'talked', 'painter',)
    ordering = ('title', 'description', 'created', 'youtube_link', 'talked', 'painter',)
    

@admin.register(Intervyu_piece)
class Intervyu_pieceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'intervyu',)
    list_filter = ('title', 'description', 'intervyu',)
    search_fields = ('title', 'description', 'intervyu',)
    ordering = ('title', 'description', 'intervyu',)
    

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)
    list_filter = ('title', 'description',)
    search_fields = ('title', 'description',)
    ordering = ('title', 'description',)
    

@admin.register(Bisnes_new)
class Bisnes_newAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created',)
    list_filter = ('title', 'description', 'created',)
    search_fields = ('title', 'description', 'created',)
    ordering = ('title', 'description', 'created',)
    

@admin.register(Bisnes_new_piece)
class Bisnes_new_pieceAdmin(admin.ModelAdmin):
    list_display = ('description', 'bisnes_new',)
    list_filter = ('description', 'bisnes_new',)
    search_fields = ('description', 'bisnes_new',)
    ordering = ('description', 'bisnes_new',)
    

@admin.register(Video_new)
class Video_newAdmin(admin.ModelAdmin):
    list_display = ('title','created',)
    list_filter = ('title','created',)
    search_fields = ('title', 'created',)
    ordering = ('title', 'created',)
    

@admin.register(Video_new_piece)
class Video_new_pieceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'video_new',)
    list_filter = ('title', 'description', 'video_new',)
    search_fields = ('title', 'description', 'video_new',)
    ordering = ('title', 'description', 'video_new',)
    

@admin.register(Area_new)
class Area_newAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created',)
    list_filter = ('title', 'description', 'created',)
    search_fields = ('title', 'description', 'created',)
    ordering = ('title', 'description', 'created',)
    

@admin.register(Area_new_piece)
class Area_new_pieceAdmin(admin.ModelAdmin):
    list_display = ('description', 'area_new',)
    list_filter = ('description', 'area_new',)
    search_fields = ('description', 'area_new',)
    ordering = ('description', 'area_new',)
    

@admin.register(Area_new_list)
class Area_new_listAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created',)
    list_filter = ('title', 'description', 'created',)
    search_fields = ('title', 'description', 'created',)
    ordering = ('title', 'description', 'created',)
    

@admin.register(Area_new_list_piece)
class Area_new_list_pieceAdmin(admin.ModelAdmin):
    list_display = ('description', 'area_new_list',)
    list_filter = ('description', 'area_new_list',)
    search_fields = ('description', 'area_new_list',)
    ordering = ('description', 'area_new_list',)
    