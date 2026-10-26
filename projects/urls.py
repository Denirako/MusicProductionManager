from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.project_list, name='project_list'),
    path('projects/create/', views.project_create, name='project_create'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('projects/<int:pk>/edit/', views.project_edit, name='project_edit'),
    path('projects/<int:pk>/delete/', views.project_delete, name='project_delete'),
    path('projects/<int:pk>/tasks/create/', views.task_create, name='task_create'),
    path('tasks/<int:pk>/edit/', views.task_edit, name='task_edit'),
    path('tasks/<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('projects/<int:pk>/notes/create/', views.note_create, name='note_create'),
    path('notes/<int:pk>/edit/', views.note_edit, name='note_edit'),
    path('notes/<int:pk>/delete/', views.note_delete, name='note_delete'),
    path('projects/<int:pk>/versions/create/', views.track_version_create, name='track_version_create'),
    path('versions/<int:pk>/edit/', views.track_version_edit, name='track_version_edit'),
    path('versions/<int:pk>/delete/', views.track_version_delete, name='track_version_delete'),
]
