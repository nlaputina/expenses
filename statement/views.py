from django.http import JsonResponse
from django.db.models import Q


from django.views.decorators.csrf import csrf_exempt
from .models import Expenses, Tag


def show_list_for_period(request, qs):
    start_point = request.GET.get('start_point')
    final_point = request.GET.get('final_point')
    if start_point and final_point:
        qs_period = qs.filter(date__range=(start_point, final_point))
    elif start_point and not final_point:
        qs_period = qs.filter(date__gte=start_point)
    elif final_point and not start_point:
        qs_period = qs.filter(date__lte=final_point)
    else:
        qs_period = qs
    return qs_period


def list_on_categories(request, qs_period):
    if request.GET.get('category') == 'food':
        qs_category = qs_period.filter(Q(description__contains='FROUTOPIA') | Q(description__contains='ALPHAMEGA') | Q(description__contains='sweets')|Q(description__contains='MELIS'))
    elif request.GET.get('category') == 'outside':
        qs_category = qs_period.filter(Q(description__contains='ZORBAS') | Q(description__contains='NOMAD') | Q(description__contains='WOLT')|Q(description__contains='RESTAURANT') | Q(description__contains='BAR') | Q(description__contains='COFFEE'))
    elif request.GET.get('category') == 'car':
        qs_category = qs_period.filter(Q(description__contains='ESSO') | Q(description__contains='PETROLINA'))
    elif request.GET.get('category') == 'health':
        qs_category = qs_period.filter(Q(description__contains='PHARMA') | Q(description__contains='MEDICAL'))
    elif request.GET.get('category') == 'children':
        qs_category = qs_period.filter(Q(description__contains='MAVROS') | Q(description__contains='WONDERLAND') | Q(description__contains='JUMBO'))
    else:
        qs_category = qs_period

    return qs_category


def show_expenses_by_tag(request):
    tag_id = request.GET.get('tag_id')
    qs = Expenses.objects.filter(tags=tag_id)
    tag_interested = Tag.objects.get(id=tag_id)
    dict_by_tag = {tag_interested.name: [expense.to_dict() for expense in qs]}

    return JsonResponse(dict_by_tag, safe=False)


def sum_of_transactions(qs_category):
    sum = 0
    for note in list(qs_category):
        sum += float(note.amount)
    return sum


@csrf_exempt
def show_list_expenses(request):
    qs = Expenses.objects.all()
    qs_period = show_list_for_period(request, qs)
    qs_category = list_on_categories(request, qs_period)
    number_of_operations = qs_category.count()
    sum = sum_of_transactions(qs_category)
    dict_to_show = {'total_num': number_of_operations, 'sum': sum, 'items': [note.to_dict() for note in list(qs_category)]}

    return JsonResponse(dict_to_show)


def show_list_tags(request):
    qs = Tag.objects.all()
    dict_to_show = {'items': [item.to_dict() for item in qs]}

    return JsonResponse(dict_to_show)



