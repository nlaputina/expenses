from django.urls import path

from .views import *

urlpatterns = [
    path('expenses/', show_list_expenses),
    path('tags/', show_list_tags),
    path('expenses_by_tag/', show_expenses_by_tag),
]

