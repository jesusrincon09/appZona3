from django.urls import path
from .views.index import *
from .views.sport import *
from django.conf.urls import handler404

handler404 = Custom404View.as_view()

urlpatterns = [
    path('', CustomIndexView.as_view(), name="home"),
    path('sport/', ListSportView.as_view(), name="sport_list"),
    path('sport/create/', CreateSportView.as_view(), name="sport_create"),
    path('sport/update/<int:pk>/', UpdateSportView.as_view(), name="sport_update"),
    path('sport/delete/<int:pk>/', DeleteSportView.as_view(), name="sport_delete"),
]
