# Generated by Django 2.2.3 on 2019-10-11 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20191011_1608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='slug',
        ),
    ]
