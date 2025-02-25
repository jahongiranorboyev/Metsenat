# Generated by Django 5.1.5 on 2025-02-23 13:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appeals', '0001_initial'),
        ('general', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='appeal',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='appeal',
            name='payment_method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='general.paymentmethod'),
        ),
        migrations.AddField(
            model_name='appeal',
            name='sponsor',
            field=models.ForeignKey(limit_choices_to={'role': 'sponsor'}, on_delete=django.db.models.deletion.PROTECT, related_name='appeals', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='appeal',
            name='updated_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='appeal',
            unique_together={('sponsor', 'phone_number')},
        ),
    ]
