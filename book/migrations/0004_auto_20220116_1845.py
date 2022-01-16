# Generated by Django 3.2.10 on 2022-01-16 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20220116_1836'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'نویسنده', 'verbose_name_plural': 'نویسندگان'},
        ),
        migrations.AlterModelOptions(
            name='translator',
            options={'verbose_name': 'مترجم', 'verbose_name_plural': 'مترجمان'},
        ),
        migrations.AlterField(
            model_name='author',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='./images/person/', verbose_name='عکس پروفایل'),
        ),
        migrations.AlterField(
            model_name='author',
            name='middle_name',
            field=models.CharField(max_length=75, null=True, verbose_name='نام میانی'),
        ),
        migrations.AlterField(
            model_name='translator',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='./images/person/', verbose_name='عکس پروفایل'),
        ),
        migrations.AlterField(
            model_name='translator',
            name='middle_name',
            field=models.CharField(max_length=75, null=True, verbose_name='نام میانی'),
        ),
    ]