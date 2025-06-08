from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views.index import *
from .views.sport import *
from .views.schedules import *
from .views.company import *
from .views.spaces import *
from .views.reservation import *
from .views.users import *
from .views.roles import *
from .views.login import *
from django.conf.urls import handler404
from django.contrib.auth import views as auth_views

handler404 = Custom404View.as_view()

urlpatterns = [
    #Login
    path('', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    #Home
    path('home/', CustomIndexView.as_view(), name="home"),
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
    path('spaces/ajax/<int:pk>/', AjaxSpacesByIdView.as_view(), name="spaces_ajax"),
    #Reservation
    path('reservation/', ListReservationView.as_view(), name="reservation_list"),
    path('reservation/create/', CreateReservationView.as_view(), name="reservation_create"),
    path('reservation/update/<int:pk>/', UpdateReservationView.as_view(), name="reservation_update"),
    path('reservation/delete/<int:pk>/', DeleteReservationView.as_view(), name="reservation_delete"),
    #Users
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/create/', UserCreateView.as_view(), name='user_create'),
    path('users/<int:pk>/edit/', UserUpdateView.as_view(), name='user_update'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
    path('users/<int:pk>/permissions/', UserPermissionUpdateView.as_view(), name='user_permissions'),
    path('user/recover/password/', Recoverpassword.as_view(), name='recovery_password'),
    path('reset/<uidb64>/<token>/',CustomPasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    #Roles
    path('roles/', RoleListView.as_view(), name='role_list'),
    path('roles/create/', RoleCreateView.as_view(), name='role_create'),
    path('roles/<int:pk>/update/', RoleUpdateView.as_view(), name='role_update'),
    path('roles/<int:pk>/delete/', RoleDeleteView.as_view(), name='role_delete'),

]  + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
