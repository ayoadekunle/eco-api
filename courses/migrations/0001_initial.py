# Generated by Django 4.0.3 on 2022-04-16 13:13

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('title', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=55, primary_key=True, serialize=False, unique=True)),
                ('is_starred', models.BooleanField(default=False)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('expiry_date', models.DateField()),
                ('color', colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=18, samples=None)),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
    ]
