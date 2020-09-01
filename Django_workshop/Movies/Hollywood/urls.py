from django.urls import path
from Hollywood import views

urlpatterns = [
	path('home/',views.home),
]