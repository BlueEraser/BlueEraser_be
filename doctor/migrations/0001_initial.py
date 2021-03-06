# Generated by Django 3.2.8 on 2021-10-28 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('user', models.OneToOneField(db_column='user', on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='doctor', serialize=False, to='user.user')),
                ('hospital_address', models.CharField(max_length=200, null=True, verbose_name='병원주소')),
                ('is_verified', models.BooleanField(default=False, null=True, verbose_name='인가여부')),
                ('self_pr', models.TextField(null=True, verbose_name='자기소개')),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_name', models.CharField(max_length=50, verbose_name='자격종류')),
                ('certificate_image', models.ImageField(upload_to='')),
                ('doctor', models.ForeignKey(db_column='doctor', on_delete=django.db.models.deletion.CASCADE, related_name='certificates', to='doctor.doctor')),
            ],
        ),
    ]
