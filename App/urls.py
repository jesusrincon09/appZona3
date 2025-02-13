from django.urls import path
from .views.index import *
from .views.sport import *
from .views.schedules import *
from django.conf.urls import handler404

handler404 = Custom404View.as_view()

urlpatterns = [
    path('', CustomIndexView.as_view(), name="home"),
    path('sport/', ListSportView.as_view(), name="sport_list"),
    path('sport/create/', CreateSportView.as_view(), name="sport_create"),
    path('sport/update/<int:pk>/', UpdateSportView.as_view(), name="sport_update"),
    path('sport/delete/<int:pk>/', DeleteSportView.as_view(), name="sport_delete"),
    path('schedules/', ListScheduleView.as_view(), name="schedules_list"),
    path('schedules/create/', CreateScheduleView.as_view(), name="schedules_create"),
    path('schedules/update/<int:pk>/', UpdateScheduleView.as_view(), name="schedules_update"),
    path('schedules/delete/<int:pk>/', DeleteScheduleView.as_view(), name="schedules_delete"),
]
