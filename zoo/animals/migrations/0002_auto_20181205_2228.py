# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-05 22:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='food', to='animals.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Spiece',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('countries', models.ManyToManyField(related_name='spieces', to='animals.Country')),
                ('foods', models.ManyToManyField(related_name='spieces', to='animals.Food')),
            ],
        ),
        migrations.CreateModel(
            name='Zoo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='zoos', to='animals.Country')),
            ],
        ),
        migrations.DeleteModel(
            name='Duck',
        ),
        migrations.DeleteModel(
            name='Lion',
        ),
        migrations.AddField(
            model_name='animal',
            name='foods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animals', to='animals.Food'),
        ),
        migrations.AddField(
            model_name='animal',
            name='spiece',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animals.Spiece'),
        ),
    ]
