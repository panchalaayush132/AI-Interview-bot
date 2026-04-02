from django.urls import path
from . import views

app_name = 'candidates'

urlpatterns = [
    path('', views.upload_resume, name='upload_resume'),
    path('success/', views.upload_success, name='upload_success'),
    path('hr/', views.hr_dashboard, name='hr_dashboard'),
]
