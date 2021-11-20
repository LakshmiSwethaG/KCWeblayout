from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('topic/part<int:part_num>/chap<int:chap_num>/', views.topic_detail, name='topic_detail'),
]