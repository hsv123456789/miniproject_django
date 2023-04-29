# Generated by Django 4.1.8 on 2023-04-29 02:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(1)])),
                ('password', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(1)])),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
