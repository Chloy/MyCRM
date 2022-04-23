from django.urls import path
from . import views
from django.contrib.auth.views import LoginView


app_name = 'crm_app'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('gangster/create/', views.GangsterCreate.as_view(), name='gangster_create'),
    path('gangster/<int:pk>/', views.GangsterDetail.as_view(), name='gangster_detail'),
    path('gangster/<int:pk>/update', views.GangsterUpdate.as_view(), name='gangster_update'),
    path('gangster/<int:pk>/delete', views.GangsterDelete.as_view(), name='gangster_delete'),
    path('login', LoginView.as_view(), name='login'),
]