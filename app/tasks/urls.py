from django.urls import path
from . import views

app_name = "tasks"  #prevent same name collision 

urlpatterns = [
    path("", views.index, name="tasks"),
    path("add/", views.add, name="add"),
]