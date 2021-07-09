from django.urls import path
from . import views

urlpatterns = [
    path("",views.all_tasks,name="all-task"),
    path("<slug:slug>",views.detail_task,name="task-page"),
]