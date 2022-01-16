# Generated by Django 3.2.10 on 2022-01-16 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0013_auto_20220116_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='teller',
            field=models.ManyToManyField(to='book.Teller', verbose_name='مترجم'),
        ),
        migrations.AlterField(
            model_name='book',
            name='translator',
            field=models.ManyToManyField(to='book.Translator', verbose_name='مترجم'),
        ),
    ]
