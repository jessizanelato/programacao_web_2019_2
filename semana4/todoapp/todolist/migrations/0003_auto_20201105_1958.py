# Generated by Django 3.1.3 on 2020-11-05 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_auto_20201105_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
