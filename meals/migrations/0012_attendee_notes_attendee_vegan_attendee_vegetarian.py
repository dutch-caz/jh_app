# Generated by Django 5.0.2 on 2024-04-18 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0011_announcement'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendee',
            name='notes',
            field=models.TextField(blank=True, verbose_name='Notes'),
        ),
        migrations.AddField(
            model_name='attendee',
            name='vegan',
            field=models.BooleanField(default=False, verbose_name='Vegan'),
        ),
        migrations.AddField(
            model_name='attendee',
            name='vegetarian',
            field=models.BooleanField(default=False, verbose_name='Vegetarian'),
        ),
    ]