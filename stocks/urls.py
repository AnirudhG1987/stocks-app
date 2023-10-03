"""stocks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ci/',include('ci_app.urls')),
    path('charts/',include('scharts.urls')),
    path('options/',include('options.urls')),
    path('tictactoe/', include('tictactoe.urls')),
    path('worksheet/', include('worksheet.urls')),
    path('', include('home.urls')),
    path('margin/', include('margin_app.urls')),
    path('sudoku/', include('sudoku.urls')),

]
