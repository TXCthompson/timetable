from django.http import HttpResponse
from django.shortcuts import render
from .models import Group, GroupTimetable
from django.shortcuts import redirect
from django.shortcuts import render
import datetime

def index(request):
    if request.method == "GET" and 'group_name' in request.GET:
        group_name = request.GET['group_name']
        return redirect("group", group_name)
    
    return render(request, "timetable/index.html", {
        "groups_list": Group.objects.all()
    })


def group_d(request, group_name):
    
    if request.method == "GET" and 'group_name' in request.GET:
        group_name = request.GET['group_name']
        return redirect("group", group_name)
    
    else: 
        group_names = Group.objects.values_list('group_name', flat=True)
        if group_name in group_names:
            group = Group.objects.get(group_name=group_name)
            group_id = group.id
            
            current_day = datetime.datetime.today().weekday()

            days_of_week = ['Понеділок', 'Вівторок', 'Середа', 'Четвер', "П'ятниця", 'Субота']
            
            return render(request, "timetable/time_table_page.html", {
                "group_name": group_name,
                "group_time": GroupTimetable.objects.filter(group_name_id=group_id).order_by('time_s'),
                'current_day': current_day,
                'days_of_week': days_of_week,
                "groups_list": Group.objects.all()
            })
        else:
            return render(request, "timetable/error_page.html")


    