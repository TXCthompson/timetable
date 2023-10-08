# Generated by Django 4.2.5 on 2023-09-21 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': 'Група', 'verbose_name_plural': 'Групи'},
        ),
        migrations.AlterModelOptions(
            name='grouptimetable',
            options={'ordering': ['group_name', 'day'], 'verbose_name': 'Розклад', 'verbose_name_plural': 'Розклади'},
        ),
        migrations.AlterModelOptions(
            name='typesl',
            options={'verbose_name': 'Тип пари', 'verbose_name_plural': 'Типи пар'},
        ),
        migrations.AlterField(
            model_name='days',
            name='day',
            field=models.CharField(max_length=10, verbose_name='День'),
        ),
        migrations.AlterField(
            model_name='group',
            name='group_name',
            field=models.CharField(max_length=10, verbose_name='Група'),
        ),
        migrations.AlterField(
            model_name='grouptimetable',
            name='cabinet',
            field=models.IntegerField(verbose_name='Аудиторія'),
        ),
        migrations.AlterField(
            model_name='grouptimetable',
            name='day',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dayname', to='timetable.days', verbose_name='День'),
        ),
        migrations.AlterField(
            model_name='grouptimetable',
            name='group_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groupname', to='timetable.group', verbose_name='Група'),
        ),
        migrations.AlterField(
            model_name='grouptimetable',
            name='subject_name',
            field=models.CharField(max_length=64, verbose_name='Предмет'),
        ),
        migrations.AlterField(
            model_name='grouptimetable',
            name='teacher',
            field=models.CharField(max_length=64, verbose_name='Викладач'),
        ),
        migrations.AlterField(
            model_name='grouptimetable',
            name='time_e',
            field=models.TimeField(verbose_name='Кінець'),
        ),
        migrations.AlterField(
            model_name='grouptimetable',
            name='time_s',
            field=models.TimeField(verbose_name='Початок'),
        ),
        migrations.AlterField(
            model_name='grouptimetable',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='typename', to='timetable.typesl', verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='typesl',
            name='type_l',
            field=models.CharField(max_length=15, verbose_name='Тип'),
        ),
    ]
