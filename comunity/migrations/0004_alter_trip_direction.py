# Generated by Django 5.0 on 2023-12-18 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comunity', '0003_alter_trip_direction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='direction',
            field=models.IntegerField(choices=[(0, 'من الجامعة'), (1, 'إلى الجامعة')]),
        ),
    ]
