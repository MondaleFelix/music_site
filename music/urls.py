from django.urls import path
from . import views

urlpatterns = [
	path('', views.musicians, name='home'),
	path('musician_detail/<int:id>', views.musician_detail, name='musician_detail'),

]