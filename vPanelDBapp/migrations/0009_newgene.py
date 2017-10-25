# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-09-26 10:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vPanelDBapp', '0008_auto_20170925_1536'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewGene',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gene_Name', models.CharField(max_length=200)),
                ('Gene_IDs', models.TextField()),
                ('Transcript_IDs', models.TextField(blank=True, null=True)),
                ('Virtual_Panels', models.NullBooleanField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
