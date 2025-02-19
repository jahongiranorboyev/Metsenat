# Generated by Django 5.1.5 on 2025-02-18 04:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentsponsor',
            name='student',
            field=models.ForeignKey(limit_choices_to={'necessary_balance__gt': 0, 'role': 'student'}, on_delete=django.db.models.deletion.PROTECT, related_name='student_sponsors', to=settings.AUTH_USER_MODEL),
        ),
    ]
