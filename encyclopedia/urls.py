from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.title, name="title"),
    path("search", views.search, name="search"),
    path("create", views.create, name="create"),
    path("edit/<str:edit_title>", views.edit, name="edit"),
    path("edit/wiki/<str:title>", views.title, name="edited"),
    path("random", views.random_page, name="random")
]
