# Generated by Django 5.0.7 on 2024-07-13 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adopet', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutor',
            name='email',
        ),
        migrations.RemoveField(
            model_name='tutor',
            name='nome',
        ),
    ]
