# Generated by Django 3.2.10 on 2022-02-26 18:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0009_auto_20220205_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='audiobook',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='author',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='category',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='electronicbook',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='physicalbook',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='publisher',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='teller',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='translator',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='audiobook',
            name='price_unit',
            field=models.CharField(blank=True, choices=[('FRE', '---'), ('IRR', 'تومان ایران'), ('USD', 'دلار آمریکا'), ('GBP', 'پوند انگلیس'), ('CAD', 'دلار کانادا'), ('AUD', 'دلار استرالیا')], default='FRE', max_length=3, null=True, verbose_name='واحد پول'),
        ),
        migrations.AlterField(
            model_name='electronicbook',
            name='price_unit',
            field=models.CharField(blank=True, choices=[('FRE', '---'), ('IRR', 'تومان ایران'), ('USD', 'دلار آمریکا'), ('GBP', 'پوند انگلیس'), ('CAD', 'دلار کانادا'), ('AUD', 'دلار استرالیا')], default='FRE', max_length=3, null=True, verbose_name='واحد پول'),
        ),
        migrations.AlterField(
            model_name='physicalbook',
            name='price_unit',
            field=models.CharField(blank=True, choices=[('FRE', '---'), ('IRR', 'تومان ایران'), ('USD', 'دلار آمریکا'), ('GBP', 'پوند انگلیس'), ('CAD', 'دلار کانادا'), ('AUD', 'دلار استرالیا')], default='FRE', max_length=3, null=True, verbose_name='واحد پول'),
        ),
    ]
