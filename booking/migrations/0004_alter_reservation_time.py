# Generated by Django 4.2.18 on 2025-02-19 18:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_alter_reservation_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
