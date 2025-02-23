from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views.index import *
from .views.sport import *
from .views.schedules import *
from .views.company import *
from .views.spaces import *
from django.conf.urls import handler404

handler404 = Custom404View.as_view()

urlpatterns = [
    #Home
    path('', CustomIndexView.as_view(), name="home"),
    #Sport
    path('sport/', ListSportView.as_view(), name="sport_list"),
    path('sport/create/', CreateSportView.as_view(), name="sport_create"),
    path('sport/update/<int:pk>/', UpdateSportView.as_view(), name="sport_update"),
    path('sport/delete/<int:pk>/', DeleteSportView.as_view(), name="sport_delete"),
    #Schedules
    path('schedules/', ListScheduleView.as_view(), name="schedules_list"),
    path('schedules/create/', CreateScheduleView.as_view(), name="schedules_create"),
    path('schedules/update/<int:pk>/', UpdateScheduleView.as_view(), name="schedules_update"),
    path('schedules/delete/<int:pk>/', DeleteScheduleView.as_view(), name="schedules_delete"),
    #Company
    path('company/create/', CreateCompanyView.as_view(), name="company_create"),
    path('company/update/<int:pk>/', UpdateCompanyView.as_view(), name="company_update"),
    #Spaces
    path('spaces/', ListSpacesView.as_view(), name="spaces_list"),
    path('spaces/create/', CreateSpacesView.as_view(), name="spaces_create"),
    path('spaces/update/<int:pk>/', UpdateSpacesView.as_view(), name="spaces_update"),
    path('spaces/delete/<int:pk>/', DeleteSpacesView.as_view(), name="spaces_delete"),
]  + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
