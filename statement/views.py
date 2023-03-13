from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models import Q
from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from .models import *


@csrf_exempt
def show_list_expenses(request):
    qs = Expenses.objects.all()
    return JsonResponse([note.to_dict() for note in qs], safe=False)


@csrf_exempt
def show_list_for_period(request):
    start_point = request.GET.get('start_point')
    final_point = request.GET.get('final_point')
    list_for_period = Expenses.objects.filter(date__range=(start_point, final_point))
    return JsonResponse([note.to_dict() for note in list_for_period], safe=False)


def list_on_categories(request):
    if request.GET.get('category') == 'food':
        qs = Expenses.objects.filter(Q(description__contains='FROUTOPIA') | Q(description__contains='ALPHAMEGA') | Q(description__contains='sweets')|Q(description__contains='MELIS'))
    elif request.GET.get('category') == 'outside':
        qs = Expenses.objects.filter(Q(description__contains='ZORBAS') | Q(description__contains='NOMAD') | Q(description__contains='WOLT')|Q(description__contains='RESTAURANT') | Q(description__contains='BAR') | Q(description__contains='COFFEE'))
    elif request.GET.get('category') == 'car':
        qs = Expenses.objects.filter(Q(description__contains='ESSO') | Q(description__contains='PETROLINA'))
    elif request.GET.get('category') == 'health':
        qs = Expenses.objects.filter(Q(description__contains='PHARMA') | Q(description__contains='MEDICAL'))
    elif request.GET.get('category') == 'children':
        qs = Expenses.objects.filter(Q(description__contains='MAVROS') | Q(description__contains='WONDERLAND') | Q(description__contains='JUMBO'))
    list_category = list(qs)
    return JsonResponse([note.to_dict() for note in list_category], safe=False)