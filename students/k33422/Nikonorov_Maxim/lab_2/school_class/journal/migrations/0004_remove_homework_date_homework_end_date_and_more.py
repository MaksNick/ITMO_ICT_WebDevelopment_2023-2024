# Generated by Django 4.2.6 on 2023-10-08 11:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0003_homework_date_homework_grade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homework',
            name='date',
        ),
        migrations.AddField(
            model_name='homework',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 8, 14, 14, 34, 146501)),
        ),
        migrations.AddField(
            model_name='homework',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 8, 14, 14, 34, 146501)),
        ),
        migrations.AlterField(
            model_name='homework',
            name='grade',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
