from django.urls import path
from . import views

urlpatterns=[
    path("<int:month>",views.intindex),
    path("<str:month>",views.index,name="monthly-challenges"),
    path("",views.month_list),
]