# Generated by Django 3.2 on 2021-04-20 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employees',
            old_name='DeteOfJoining',
            new_name='DateOfJoining',
        ),
        migrations.RenameField(
            model_name='employees',
            old_name='EmployeesId',
            new_name='EmployeeId',
        ),
    ]
