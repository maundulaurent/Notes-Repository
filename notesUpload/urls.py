from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('files', views.my_files, name="my_files"),
    path('delete/<int:file_id>/', views.delete_file, name="delete_file"),
]