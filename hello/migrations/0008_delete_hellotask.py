# Generated by Django 4.0.5 on 2022-12-23 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0007_alter_employee_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HelloTask',
        ),
    ]
