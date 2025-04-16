from django.urls import path
from . import views

urlpatterns = [
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('add-profile/', views.add_profile, name='add_profile'),
    path('history/', views.view_history, name='view_history'),
    path('add/', views.add_record, name='add_record'),
    path('edit_record/<int:record_id>/', views.edit_record, name='edit_record'),
    path('delete_record/<int:record_id>/', views.delete_record, name='delete_record'),
]
