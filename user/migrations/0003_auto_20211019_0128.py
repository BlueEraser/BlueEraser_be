# Generated by Django 3.2.8 on 2021-10-18 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20211018_2153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_doctor',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_patient',
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('P', 'Patient'), ('D', 'Doctor')], default='P', max_length=2, verbose_name='유저타입'),
        ),
    ]
