# Generated by Django 5.0.2 on 2024-03-08 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0004_attendee_type_alter_attendance_unique_together'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendee',
            name='type',
        ),
        migrations.AddField(
            model_name='attendee',
            name='half_plates',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='Half Plates'),
        ),
    ]
