from django.urls import path, re_path
from tictactoe import views


urlpatterns = [
    # this goes from admin folder
    path('', views.index,name='index'),
    path('my-ajax-test/', views.myajaxtestview, name='ajax-test-view'),
]
