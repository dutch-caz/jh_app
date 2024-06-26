# Generated by Django 5.0.2 on 2024-03-04 08:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='attendee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('gluten_free', models.BooleanField(default=False, verbose_name='Gluten Free')),
                ('dairy_free', models.BooleanField(default=False, verbose_name='Dairy Free')),
                ('vegan', models.BooleanField(default=False, verbose_name='Vegan')),
            ],
        ),
        migrations.CreateModel(
            name='attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('present', models.BooleanField(default=False, verbose_name='Present')),
                ('attendee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='meals.attendee')),
            ],
        ),
        migrations.CreateModel(
            name='meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Meal Name')),
                ('description', models.TextField(blank=True, verbose_name='Meal Description')),
                ('meal_type', models.CharField(choices=[('breakfast', 'Breakfast'), ('lunch', 'Lunch'), ('dinner', 'Dinner')], default='breakfast', max_length=30, verbose_name='Meal Type')),
                ('start_time', models.DateTimeField(verbose_name='Start Time and Date')),
                ('end_time', models.DateTimeField(verbose_name='End Time and Date')),
                ('latitude', models.DecimalField(decimal_places=7, max_digits=40, verbose_name='Set Latitude')),
                ('longitude', models.DecimalField(decimal_places=7, max_digits=40, verbose_name='Set Longitude')),
                ('people_attending', models.ManyToManyField(blank=True, null=True, through='meals.attendance', to='meals.attendee')),
            ],
        ),
        migrations.AddField(
            model_name='attendance',
            name='meal',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='meals.meal'),
        ),
        migrations.AlterUniqueTogether(
            name='attendance',
            unique_together={('attendee', 'meal')},
        ),
    ]
