# Generated by Django 3.2.10 on 2022-01-29 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20220129_2203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audiobook',
            name='category',
        ),
        migrations.AddField(
            model_name='audiobook',
            name='category',
            field=models.ManyToManyField(blank=True, to='book.Category', verbose_name='دسته\u200cبندی'),
        ),
        migrations.RemoveField(
            model_name='electronicbook',
            name='category',
        ),
        migrations.AddField(
            model_name='electronicbook',
            name='category',
            field=models.ManyToManyField(blank=True, to='book.Category', verbose_name='دسته\u200cبندی'),
        ),
        migrations.RemoveField(
            model_name='physicalbook',
            name='category',
        ),
        migrations.AddField(
            model_name='physicalbook',
            name='category',
            field=models.ManyToManyField(blank=True, to='book.Category', verbose_name='دسته\u200cبندی'),
        ),
    ]