# Generated by Django 4.1.3 on 2022-11-09 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('author', models.CharField(max_length=50, verbose_name='Автор')),
                ('price', models.IntegerField(verbose_name='Стоимость')),
                ('description', models.TextField(verbose_name='Описание')),
                ('address', models.TextField(verbose_name='Адрес')),
                ('is_publisher', models.BooleanField(verbose_name='Опубликована')),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
            ],
        ),
    ]
