from django.urls import path
from . import views


app_name = 'crm_app'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('gangster/create/', views.gangster_create, name='gangster_create'),
    path('gangster/<int:pk>/', views.gangster_detail, name='gangster_detail'),
    path('gangster/<int:pk>/update', views.gangster_update, name='gangster_update'),
    path('gangster/<int:pk>/delete', views.gangster_delete, name='gangster_delete'),
]