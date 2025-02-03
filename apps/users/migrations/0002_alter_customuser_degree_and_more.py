# Generated by Django 5.1.5 on 2025-02-01 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='degree',
            field=models.CharField(blank=True, choices=[('bachelor', 'Bachelor'), ('magister', 'Magister'), ('empty', 'Empty')], default='empty', max_length=10),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='sponsor_type',
            field=models.CharField(blank=True, choices=[('physical', 'Physical'), ('legal', 'Legal'), ('empty', 'Empty')], default='empty', max_length=20),
        ),
    ]
