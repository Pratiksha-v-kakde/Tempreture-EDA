import csv
import xlwt
from django.shortcuts import render
from django.http import HttpResponse
from .models import MonthlyTemperature
import itertools


def index(request):
    return render(request, 'chartapp/index.html')


def export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="temperatures.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Temperatures')

    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['YEAR', 'JAN', 'FEB', 'MAR', 'APR',
               'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT',
               'NOV',
               'DEC']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()

    rows = MonthlyTemperature.objects.all().values_list('YEAR', 'JAN', 'FEB', 'MAR', 'APR',
                                                        'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT',
                                                        'NOV',
                                                        'DEC')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="temperatures.csv"'

    writer = csv.writer(response)
    writer.writerow(['YEAR', 'JAN', 'FEB', 'MAR', 'APR',
                     'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT',
                     'NOV',
                     'DEC'])

    users = MonthlyTemperature.objects.all().values_list('YEAR', 'JAN', 'FEB', 'MAR', 'APR',
                                                         'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT',
                                                         'NOV',
                                                         'DEC')
    for user in users:
        writer.writerow(user)

    return response


def explore(request):
    years = MonthlyTemperature.objects.all()
    selectval = 0
    if request.method == "POST":
        selectval = request.POST.get('years')
    inputs = MonthlyTemperature.objects.all().filter(id=selectval).values_list('YEAR', 'JAN', 'FEB', 'MAR', 'APR',
                                                                               'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT',
                                                                               'NOV',
                                                                               'DEC')

    select_year = MonthlyTemperature.objects.all().filter(id=selectval).values_list('YEAR')
    mylist1 = []
    mylist3 = ['JAN', 'FEB', 'MAR', 'APR',
               'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT',
               'NOV',
               'DEC']

    for key in inputs:
        mylist1.append(key[1:])
    mylist2 = list(itertools.chain.from_iterable(mylist1))
    select_year1 = list(itertools.chain.from_iterable(select_year))

    if len(mylist2) != 0:
        min_val = min(mylist2)
        max_val = max(mylist2)
        min_pos = mylist2.index(min(mylist2))
        pos1 = mylist3[min_pos]
        max_pos = mylist2.index(max(mylist2))
        pos2 = mylist3[max_pos]
        avg = sum(mylist2) / len(mylist2)
        average = round(avg, 2)
    else:
        pos1 = 0
        pos2 = 0
        average = 0
        min_val = 0
        max_val = 0
    context = {'years': years, 'mylist2': mylist2, 'selectval': select_year1, 'min_pos': pos1, 'max_pos': pos2,
               'average': average, 'min_val': min_val, 'max_val': max_val}
    return render(request, 'chartapp/explore.html', context)
