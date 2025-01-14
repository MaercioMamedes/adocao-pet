# Generated by Django 5.0.7 on 2024-07-13 13:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('raca', models.CharField(max_length=255)),
                ('porte', models.CharField(max_length=255)),
                ('peso', models.FloatField()),
                ('tipo_animal', models.CharField(max_length=255)),
                ('idade', models.IntegerField()),
                ('status', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
                ('tipo_arquivo', models.CharField(max_length=255)),
                ('id_animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adopet.animal')),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('telefone', models.IntegerField()),
                ('whatsapp', models.IntegerField()),
                ('cidade', models.CharField(max_length=255)),
                ('estado', models.CharField(max_length=255)),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='animal',
            name='id_tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adopet.tutor'),
        ),
    ]
