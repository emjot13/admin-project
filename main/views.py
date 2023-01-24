from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render, redirect


import database.client as database
import json


def start(request):
    return render(request, "start.html")


def admin(request):
    if request.method == "GET":
        start_date = request.GET.get("start_date", None)
        end_date = request.GET.get("end_date", None)
        users_data = database.get_admin_data_between_dates(start_date=start_date, end_date=end_date)
        users_data = dict(sorted(users_data.items()))
        for day in users_data:
            users_data[day]['hours'] = sorted(users_data[day]['hours'], key=lambda x: x['hour'])
        users_data_list = []
        for day in users_data:
            obj = users_data[day]
            obj['day'] = day
            users_data_list.append(obj)
        context = {
            'items': users_data_list,
        }
        return render(request, "admin_view.html", context)



