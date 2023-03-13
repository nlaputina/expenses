from django.urls import path

from .views import *

urlpatterns = [
    path('', show_list_expenses),
    path('period_list/', show_list_for_period),
    path('list_on_categories/', list_on_categories)
]
