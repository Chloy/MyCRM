from django.urls import path
from . import views


app_name = 'crm_app'
urlpatterns = [
    path('', views.home, name='crm_home'),
    path('gangster/create/', views.gangster_create, name='crm_gangster_create'),
    path('gangster/<int:pk>/', views.gangster_detail, name='crm_gangster_detail'),
]