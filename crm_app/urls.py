from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


app_name = 'crm_app'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('gang/all', views.Gangs.as_view(), name='gangs'),
    path('gang/create', views.GangCreate.as_view(), name='gang_create'),
    path('gang/detail/<int:pk>', views.GangDetail.as_view(), name='gang_detail'),
    path('gang/update/<int:pk>', views.GangUpdate.as_view(), name='gang_update'),
    path('gang/delete/<int:pk>', views.GangDelete.as_view(), name='gang_delete'),
    path('skirmish/create/', views.CreateSkirmish.as_view(), name='skirmish_create'),
    path('gangster/<int:pk>/', views.GangsterDetail.as_view(), name='gangster_detail'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('signup', views.SignUp.as_view(), name='signup'),
]