from django.urls import path
from options import views

urlpatterns = [
    # this goes from admin folder
    path('', views.index,name='index'),
    path('expiry_ajax/', views.expiryview, name='option_ajax'),
    path('spot_ajax/', views.spotview, name='spot_ajax'),
    path('strike_ajax/', views.strikeview, name='strike_ajax'),
]
