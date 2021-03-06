# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-08 07:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0002_auto_20160407_1243'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='advertisement',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='advertisement_images/'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='phone_number',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='zipcode',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='advertisements.City'),
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='advertisements.City'),
        ),
    ]
