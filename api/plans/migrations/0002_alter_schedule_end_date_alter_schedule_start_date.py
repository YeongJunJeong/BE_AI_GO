# Generated by Django 5.0.1 on 2024-02-27 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='end_date',
            field=models.DateTimeField(verbose_name='일정종료시각'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='start_date',
            field=models.DateTimeField(verbose_name='일정시작시각'),
        ),
    ]
