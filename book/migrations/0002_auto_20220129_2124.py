# Generated by Django 3.2.10 on 2022-01-29 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audiobook',
            name='rate',
        ),
        migrations.RemoveField(
            model_name='electronicbook',
            name='rate',
        ),
        migrations.RemoveField(
            model_name='physicalbook',
            name='rate',
        ),
        migrations.AddField(
            model_name='audiobook',
            name='user_rate',
            field=models.SmallIntegerField(blank=True, choices=[(1, 'بد'), (2, 'بد نبود'), (3, 'معمولی'), (4, 'خوب'), (5, 'عالی')], default=None, null=True, verbose_name='امتیاز'),
        ),
        migrations.AddField(
            model_name='electronicbook',
            name='user_rate',
            field=models.SmallIntegerField(blank=True, choices=[(1, 'بد'), (2, 'بد نبود'), (3, 'معمولی'), (4, 'خوب'), (5, 'عالی')], default=None, null=True, verbose_name='امتیاز'),
        ),
        migrations.AddField(
            model_name='physicalbook',
            name='user_rate',
            field=models.SmallIntegerField(blank=True, choices=[(1, 'بد'), (2, 'بد نبود'), (3, 'معمولی'), (4, 'خوب'), (5, 'عالی')], default=None, null=True, verbose_name='امتیاز'),
        ),
    ]