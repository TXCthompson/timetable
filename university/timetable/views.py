from django.http import HttpResponse
from django.shortcuts import render
from .models import Group, GroupTimetable
from django.shortcuts import redirect
import datetime

def index(request):
    if request.method == "GET" and 'group_name' in request.GET:
        group_name = request.GET['group_name']
        return redirect("group", group_name)
    
    return render(request, "timetable/index.html", {
        "groups_list": Group.objects.all()
    })

# def group_d(request, group_name):
    
#     if request.method == "GET" and 'group_name' in request.GET:
#         group_name = request.GET['group_name']
#         return redirect("group", group_name)
    
#     else: 
#         group_names = Group.objects.values_list('group_name', flat=True)
#         if group_name in group_names:
#             group = Group.objects.get(group_name=group_name)
#             group_id = group.id
            
#             current_day = datetime.datetime.today().weekday()

#             days_of_week = ['Понеділок', 'Вівторок', 'Середа', 'Четвер', "П'ятниця", 'Субота']
            
#             return render(request, "timetable/time_table_page.html", {
#                 "group_name": group_name,
#                 "group_time": GroupTimetable.objects.filter(group_name_id=group_id).order_by('time_s'),
#                 'current_day': current_day,
#                 'days_of_week': days_of_week,
#                 "groups_list": Group.objects.all()
#             })
#         else:
#             return render(request, "timetable/error_page.html")

from datetime import timedelta

def group_d(request, group_name):
    if request.method == "GET" and 'group_name' in request.GET:
        group_name = request.GET['group_name']
        return redirect("group", group_name)
    else:
        group_names = Group.objects.values_list('group_name', flat=True)
        if group_name in group_names:
            group = Group.objects.get(group_name=group_name)
            group_id = group.id

            current_date = datetime.date.today()
            start_of_week = current_date - timedelta(days=current_date.weekday())
            end_of_week = start_of_week + timedelta(days=6)

            days_of_week = ['Понеділок', 'Вівторок', 'Середа', 'Четвер', 'П\'ятниця', 'Субота']

            group_time_current_week = GroupTimetable.objects.filter(
                group_name_id=group_id,
                date_d__range=[start_of_week, end_of_week]
            ).order_by('date_d', 'time_s')

            start_of_next_week = end_of_week + timedelta(days=1)
            end_of_next_week = start_of_next_week + timedelta(days=6)

            group_time_next_week = GroupTimetable.objects.filter(
                group_name_id=group_id,
                date_d__range=[start_of_next_week, end_of_next_week]
            ).order_by('date_d', 'time_s')

            print("Current Date:", current_date)
            print("Start of Week:", start_of_week)
            print("End of Week:", end_of_week)
            print("Group Time Current Week:", group_time_current_week)
            print("Start of Next Week:", start_of_next_week)
            print("End of Next Week:", end_of_next_week)
            print("Group Time Next Week:", group_time_next_week)

            return render(request, "timetable/time_table_page.html", {
                "group_name": group_name,
                "group_time_current_week": group_time_current_week,
                "group_time_next_week": group_time_next_week,
                "current_day": current_date,
                "days_of_week": [{'name': day, 'date': start_of_week + timedelta(days=day_number)} for day_number, day in enumerate(days_of_week)],
                'days_of_next_week': [{'name': day, 'date': start_of_next_week + timedelta(days=day_number)} for day_number, day in enumerate(days_of_week)],
                "groups_list": Group.objects.all()
            })

        else:
            return render(request, "timetable/error_page.html")


