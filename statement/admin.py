from django.contrib import admin

from .models import Expenses

@admin.register(Expenses)
class ExpensesAdmin(admin.ModelAdmin):
    list_display = ['date','description','amount']
