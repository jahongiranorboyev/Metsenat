# Generated by Django 5.1.5 on 2025-02-24 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='telegram_id',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]
