# Generated by Django 3.0.5 on 2020-04-29 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_auto_20200429_0540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='length',
        ),
        migrations.RemoveField(
            model_name='song',
            name='num_stars',
        ),
    ]
