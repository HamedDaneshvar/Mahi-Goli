# Generated by Django 3.2.10 on 2022-01-29 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_auto_20220129_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiobook',
            name='listen_status',
            field=models.CharField(choices=[('U', 'شنیده نشده'), ('L', 'در حال شنیدن'), ('H', 'شنیده شده')], default='U', max_length=1, verbose_name='وضعیت'),
        ),
    ]
