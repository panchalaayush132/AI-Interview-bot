from django.urls import path
from . import views

app_name = 'interview_session'

urlpatterns = [
    path('', views.room, name='room'),
    path('api/chat/', views.api_chat, name='api_chat'),
]
