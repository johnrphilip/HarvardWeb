from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    # Add a new path for the search functionality
    path("search", views.search, name="search"),
    # ... other paths ...
]
