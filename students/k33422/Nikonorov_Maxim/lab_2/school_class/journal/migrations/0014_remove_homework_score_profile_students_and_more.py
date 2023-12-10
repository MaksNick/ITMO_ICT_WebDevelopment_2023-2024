# Generated by Django 4.2.6 on 2023-10-27 12:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('journal', '0013_alter_homework_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homework',
            name='score',
        ),
        migrations.AddField(
            model_name='profile',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='teachers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='homework',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homework',
            name='end_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='homework',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.CreateModel(
            name='HomeworkSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='homework_submissions/')),
                ('comment', models.TextField(blank=True)),
                ('homework', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journal.homework')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]