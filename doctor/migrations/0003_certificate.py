# Generated by Django 3.2.8 on 2021-10-26 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_alter_doctor_is_verified'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor', models.ForeignKey(db_column='doctor', on_delete=django.db.models.deletion.CASCADE, related_name='certificates', to='doctor.doctor')),
            ],
        ),
    ]