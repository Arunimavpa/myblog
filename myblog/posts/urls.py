from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_create, name="post_create"),
   # path("post/<int:id>/", views.post_details, name="post_details"),
    path("list/",views.post_list,name="post_list"),

]
