# Generated by Django 2.2.11 on 2020-03-31 16:40

import django_test.api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('api_key', models.CharField(default=django_test.api.models.generate_api_key, max_length=32, unique=True)),
            ],
        ),
    ]