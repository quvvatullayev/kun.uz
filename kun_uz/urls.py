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

from .views.actual import (
    CreateActual,
    GetActual,
    UpdateActual,
    DeleteActual,
)

urlpatterns += [
    path('actual/create/', CreateActual.as_view()),
    path('actual/list/', GetActual.as_view()),
    path('actual/update/<int:pk>/', UpdateActual.as_view()),
    path('actual/delete/<int:pk>/', DeleteActual.as_view()),
]

from .views.Intervyu import (
    CreateIntervyu,
    GetIntervyu,
    IntervyuList,
    UpdateIntervyu,
    DeleteIntervyu,
    DetailIntervyu,
)

urlpatterns += [
    path('intervyu/create/', CreateIntervyu.as_view()),
    path('intervyu/list/', GetIntervyu.as_view()),
    path('intervyu/list_all/', IntervyuList.as_view()),
    path('intervyu/update/<int:pk>/', UpdateIntervyu.as_view()),
    path('intervyu/delete/<int:pk>/', DeleteIntervyu.as_view()),
    path('intervyu/detail/<int:pk>/', DetailIntervyu.as_view()),
]

from .views.article import (
    CreateArticle,
    GetArticle,
    ArticleList,
    UpdateArticle,
    DeleteArticle,
    ArticleDetail,
)

urlpatterns += [
    path('article/create/', CreateArticle.as_view()),
    path('article/list/', GetArticle.as_view()),
    path('article/list_all/', ArticleList.as_view()),
    path('article/update/<int:pk>/', UpdateArticle.as_view()),
    path('article/delete/<int:pk>/', DeleteArticle.as_view()),
    path('article/detail/<int:pk>/', ArticleDetail.as_view()),
]

from .views.bisnes import (
    CreateBisnes_new,
    Bisnes_newList,
    UpdateBisnes_new,
    DeleteBisnes_new,
    DetailBisnes_new
)

urlpatterns += [
    path('bisnes_new/create/', CreateBisnes_new.as_view()),
    path('bisnes_new/lsit_all/', Bisnes_newList.as_view()),
    path('bisnes_new/update/<int:pk>/', UpdateBisnes_new.as_view()),
    path('bisnes_new/delete/<int:pk>/', DeleteBisnes_new.as_view()),
    path('bisnes_new/detail/<int:pk>/', DetailBisnes_new.as_view()),
]

from .views.home_view import (
    HomeView,
)

urlpatterns += [
    path('', HomeView.as_view()),
]