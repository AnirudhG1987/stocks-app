from django.urls import path, re_path
from .views import file_upload,delete_file


urlpatterns = [
    # this goes from admin folder
    path('upload/', file_upload, name='file_upload'),
    path('upload/delete/<int:pk>/', delete_file, name='delete_file'),
]
