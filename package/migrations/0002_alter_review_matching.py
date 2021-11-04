# Generated by Django 3.2.8 on 2021-11-04 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='matching',
            field=models.ForeignKey(db_column='matching', on_delete=django.db.models.deletion.PROTECT, related_name='review', to='package.matching'),
        ),
    ]
