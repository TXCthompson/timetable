# Generated by Django 4.2.5 on 2023-09-29 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0002_alter_group_options_alter_grouptimetable_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='grouptimetable',
            name='date_d',
            field=models.DateField(default='2023-01-01', verbose_name='Дата'),
        ),
    ]
