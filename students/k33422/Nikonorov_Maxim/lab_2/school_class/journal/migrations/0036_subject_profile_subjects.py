# Generated by Django 4.2.6 on 2023-10-28 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0035_alter_profile_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='subjects',
            field=models.ManyToManyField(blank=True, related_name='teachers', to='journal.subject'),
        ),
    ]
