from django.db import models

# Create your models here.

class Group(models.Model):
    group_name = models.CharField(max_length=10, verbose_name='Група')
    
    def __str__(self):
        return f"{self.group_name}"
    
    class Meta:
        verbose_name = 'Група'
        verbose_name_plural = 'Групи'

class Days(models.Model):
    day = models.CharField(max_length=10, verbose_name='День')
    
    def __str__(self):
        return f"{self.day}"
    
class TypesL(models.Model):
    type_l = models.CharField(max_length=15, verbose_name='Тип')
    
    def __str__(self):
        return f"{self.type_l}"
    
    class Meta:
        verbose_name = 'Тип пари'
        verbose_name_plural = 'Типи пар'

class GroupTimetable(models.Model):
    group_name = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="groupname", verbose_name='Група')
    subject_name = models.CharField(max_length=64, verbose_name='Предмет')
    type = models.ForeignKey(TypesL, on_delete=models.CASCADE, related_name="typename", verbose_name='Тип')
    day = models.ForeignKey(Days, on_delete=models.CASCADE, related_name="dayname", verbose_name='День')
    teacher = models.CharField(max_length=64, verbose_name='Викладач')
    date_d = models.DateField(verbose_name='Дата', default='2023-01-01')
    time_s = models.TimeField(verbose_name='Початок') 
    time_e = models.TimeField(verbose_name='Кінець')
    cabinet = models.IntegerField(verbose_name='Аудиторія')
    
    def __str__(self):
        return f"{self.group_name}: {self.subject_name}, {self.date_d.strftime('%d.%m')} ({self.teacher}) - {self.time_s.strftime('%H:%M')}:{self.time_e.strftime('%H:%M')}, {self.day}"
    
    class Meta:
        verbose_name = 'Розклад'
        verbose_name_plural = 'Розклади'
        ordering = ['group_name', 'day']