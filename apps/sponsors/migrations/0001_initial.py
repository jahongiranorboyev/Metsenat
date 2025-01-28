# Generated by Django 5.1.5 on 2025-01-28 09:58

import django.core.validators
import django.db.models.deletion
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appeals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentSponsor',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=50, validators=[django.core.validators.MinValueValidator(Decimal('0'))])),
                ('appeal', models.ForeignKey(limit_choices_to={'available_balance__gt': 0, 'status': 'approved'}, on_delete=django.db.models.deletion.PROTECT, related_name='appeal_studentsponsors', to='appeals.appeal')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
