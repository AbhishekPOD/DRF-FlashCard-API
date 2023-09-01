from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('cards/', views.CardList.as_view()),
    path('card/<int:id>/', views.CardDetail.as_view()),
]