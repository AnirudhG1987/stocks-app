from django.urls import path, re_path
from wordle import views


urlpatterns = [
    # this goes from admin folder
    path('', views.index,name='index'),
]
