from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('add-profile/', views.add_profile, name='add_profile'),
    path('history/', views.view_history, name='view_history'),
    path('add/', views.add_record, name='add_record'),
]
