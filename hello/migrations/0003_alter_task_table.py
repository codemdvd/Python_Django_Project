# Generated by Django 4.0.5 on 2022-12-09 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_authgroup_authgrouppermissions_authpermission_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='task',
            table='Task',
        ),
    ]