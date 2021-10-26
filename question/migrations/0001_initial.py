# Generated by Django 3.2.8 on 2021-10-26 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.JSONField()),
                ('point', models.IntegerField(verbose_name='점수')),
                ('answer_time', models.CharField(max_length=10, verbose_name='문답시간')),
                ('patient', models.ForeignKey(db_column='patient', on_delete=django.db.models.deletion.CASCADE, related_name='question', to='patient.patient')),
                ('question_form', models.ForeignKey(db_column='question_form', on_delete=django.db.models.deletion.CASCADE, related_name='question_form', to='question.questionform')),
            ],
        ),
    ]
