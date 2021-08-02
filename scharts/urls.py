from django.urls import path
from scharts import views




urlpatterns = [
    # this goes from admin folder
    path('', views.index,name='index'),
    path('chart_ajax/', views.chartview, name='chart_ajax'),

]
