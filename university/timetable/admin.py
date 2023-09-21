from django.contrib import admin
from .models import Group, GroupTimetable, TypesL
from django.db import models
from django import forms

class GroupTimetableAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'day', 'subject_name', "formatted_time_s", 'formatted_time_e')
    search_fields = ('group_name', 'subject_name', 'teacher')
    list_filter = ('group_name', 'day', 'subject_name', 'teacher')
    
    def formatted_time_s(self, obj):
        return obj.time_s.strftime('%H:%M')
    
    formatted_time_s.short_description = 'Початок'
    
    def formatted_time_e(self, obj):
        return obj.time_e.strftime('%H:%M')
    
    formatted_time_e.short_description = 'Кінець'

    formfield_overrides = {
        models.TimeField: {'widget': forms.TimeInput(format='%H:%M')}
    }

# Реєструємо ваші моделі.
admin.site.register(GroupTimetable, GroupTimetableAdmin)
admin.site.register(Group)
admin.site.register(TypesL)