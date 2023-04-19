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


def show_expenses_by_tag(request, qs_period):
    tag_id = request.GET.get('tag_id')
    qs = qs_period.filter(tags=tag_id)
    return qs


def sum_of_transactions(qs_category):
    sum = 0
    for note in list(qs_category):
        sum += float(note.amount)
    return sum


@csrf_exempt
def show_list_expenses(request):
    qs = Expenses.objects.all()
    qs_period = show_list_for_period(request, qs)
    tag_id = request.GET.get('tag_id')
    if tag_id:
        if Tag.objects.filter(id=tag_id).exists():
            qs_category = show_expenses_by_tag(request, qs_period)
        else:
            return JsonResponse("The number of tag doesn't exist", safe=False)
    else:
        qs_category = qs_period
    number_of_operations = qs_category.count()
    sum = sum_of_transactions(qs_category)
    dict_to_show = {'total_num': number_of_operations, 'sum': sum,
                    'items': [note.to_dict() for note in list(qs_category)]}
    return JsonResponse(dict_to_show)


def show_list_tags(request):
    qs = Tag.objects.all()
    dict_to_show = {'items': [item.to_dict() for item in qs]}

    return JsonResponse(dict_to_show)



