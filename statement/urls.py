from django.urls import path

from .views import *

urlpatterns = [
    path('', show_list_expenses),
]
