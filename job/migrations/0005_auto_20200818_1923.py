# Generated by Django 3.2 on 2020-08-18 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_job_published_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='Vacancy',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='job',
            name='experience',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='job',
            name='salary',
            field=models.IntegerField(default=0),
        ),
    ]