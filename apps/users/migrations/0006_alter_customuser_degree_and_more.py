# Generated by Django 5.1.5 on 2025-02-01 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_merge_20250201_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='degree',
            field=models.CharField(blank=True, choices=[('bachelor', 'Bachelor'), ('magister', 'Magister')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='sponsor_type',
            field=models.CharField(blank=True, choices=[('physical', 'Physical'), ('legal', 'Legal')], max_length=20, null=True),
        ),
    ]
