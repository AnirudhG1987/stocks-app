from django.urls import path, re_path
from sudoku import views


urlpatterns = [
    # this goes from admin folder
    path('', views.index,name='index'),
    path('solve/', views.solve_sudoku, name='solve_sudoku'),
    path('generate/', views.sudoku_gen, name='gen_sudoku')
    #path('my-ajax-test/', views.myajaxtestview, name='ajax-test-view'),
]
