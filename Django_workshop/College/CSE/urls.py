from django.contrib import admin
from django.urls import path
from CSE import views


urlpatterns = [
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('register', views.faculty_register, name='faculty_register'),
    path('update/<int:num>', views.faculty_edit, name='faculty_edit'),
]