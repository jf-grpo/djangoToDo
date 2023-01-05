# todolist/urls.py

from django.urls import path
from todolist import views

urlpatterns = [
    path("", views.index, name="index"),
    path("update_task_status/<int:task_id>/<str:new_status>/", views.update_task_status, name="update_task_status"),
    path("delete_task/<int:task_id>/", views.delete_task, name="delete_task"),
    ]