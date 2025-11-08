from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_todo, name='create_todo'),
    path('update/<int:pk>/', views.update_todo, name='update'),
    path('delete/<int:pk>/', views.delete_todo, name='delete'),
    path('toggle/<int:pk>/', views.toggle_done, name='toggle_done'),
]