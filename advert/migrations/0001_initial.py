# Generated by Django 4.2.5 on 2023-09-28 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='название')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='название')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Городы',
            },
        ),
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='дата создание')),
                ('title', models.CharField(max_length=255, verbose_name='заголовок')),
                ('description', models.TextField(verbose_name='описание')),
                ('views', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advert.category', verbose_name='каегория')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advert.city', verbose_name='город')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявлении',
            },
        ),
    ]
