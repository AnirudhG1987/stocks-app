from django.urls import path
from worksheet import views




urlpatterns = [
    # this goes from admin folder
    path('', views.index,name='index'),
    path('ajax_ws/', views.ajax_ws, name="ajax_ws"),
]
