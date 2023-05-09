from django.urls import path
from .views.new_type import (
    Create_new_type,
    List_new_type,
    Detail_new_type,
    Update_new_type,
    Delete_new_type,
)

urlpatterns = []
urlpatterns += [
    path('new_type/create/', Create_new_type.as_view()),
    path('new_type/list/', List_new_type.as_view()),
    path('new_type/detail/<int:pk>/', Detail_new_type.as_view()),
    path('new_type/update/<int:pk>/', Update_new_type.as_view()),
    path('new_type/delete/<int:pk>/', Delete_new_type.as_view()),
]

from .views.area import (
    Create_area,
    List_area,
    Detail_area,
    Update_area,
    Delete_area,
)

urlpatterns += [
    path('area/create/', Create_area.as_view()),
    path('area/list/', List_area.as_view()),
    path('area/detail/<int:pk>/', Detail_area.as_view()),
    path('area/update/<int:pk>/', Update_area.as_view()),
    path('area/delete/<int:pk>/', Delete_area.as_view()),
]

from .views.day_new import (
    Create_day_new,
    List_day_new,
    Detail_day_new,
    Update_day_new,
    Delete_day_new,
)

urlpatterns += [
    path('day_new/create/', Create_day_new.as_view()),
    path('day_new/list/', List_day_new.as_view()),
    path('day_new/detail/<int:pk>/', Detail_day_new.as_view()),
    path('day_new/update/<int:pk>/', Update_day_new.as_view()),
    path('day_new/delete/<int:pk>/', Delete_day_new.as_view()),
]