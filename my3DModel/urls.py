from django.urls import path
from . import views

urlpatterns = [
    path('', views.model_list, name='home'),
    path('home', views.model_list, name='home'),
    path('upload',views.upload_model, name='upload'),
    path('showModel/<int:modelid>/',views.showModel, name='showModel'),
    path('models', views.model_list, name='model_list'),
    path('models/upload/', views.upload_model, name='upload_model')
]