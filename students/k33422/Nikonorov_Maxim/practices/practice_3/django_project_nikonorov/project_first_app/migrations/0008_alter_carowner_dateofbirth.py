# Generated by Django 4.2.6 on 2023-11-29 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0007_alter_carowner_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carowner',
            name='DateOfBirth',
            field=models.DateField(blank=True, null=True),
        ),
    ]