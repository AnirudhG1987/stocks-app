from django.urls import path
from home import views


urlpatterns = [
    # this goes from admin folder
    path('', views.index,name='index')
]
