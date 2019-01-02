from django.urls import path
from . import views 

app_name = 'session_app'

urlpatterns = [
	path('', views.index, name='index'),
	path('contact', views.contact, name='contact'),
	path('categories', views.categories, name='categories'),
	path('selection_form', views.selection_form, name='selection_form'),
]