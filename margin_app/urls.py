from django.urls import path
from margin_app import views

urlpatterns = [
    # this goes from admin folder
    path('', views.index,name='index'),
    path('my-ajax-test/', views.myajaxtestview, name='my-ajax-test'),
]
