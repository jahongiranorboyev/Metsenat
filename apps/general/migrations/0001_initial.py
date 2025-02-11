# Generated by Django 5.1.5 on 2025-02-06 17:46

import django.core.validators
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(help_text='Enter the name of the payment method.', max_length=50, unique=True)),
                ('slug', models.SlugField(blank=True, editable=False, help_text='Slug will be automatically generated based on the name if left blank.', unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100, verbose_name='University Name')),
                ('contract_amount', models.DecimalField(decimal_places=2, max_digits=30, validators=[django.core.validators.MinValueValidator(Decimal('0'))], verbose_name='Contract Amount')),
                ('slug', models.SlugField(blank=True, editable=False, max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
