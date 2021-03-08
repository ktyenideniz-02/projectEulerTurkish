from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('soru_listesi', views.question_list, name='question_list'),
    path('soru/<int:pk>/', views.question_detail, name = 'question_detail'),
]