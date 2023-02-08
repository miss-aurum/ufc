# Generated by Django 4.1.6 on 2023-02-07 13:47

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
                ('name', models.CharField(max_length=200, verbose_name='Весовая категория')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='И.Ф.О для сотрудничества')),
                ('number', models.IntegerField(verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=254, verbose_name='Адрес электронной почты')),
                ('massage', models.CharField(max_length=200, verbose_name='Сообщения')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(max_length=200, verbose_name='Оставляют заявку и оставляют имя,  номер телефона и адрес доставки ')),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('future_info', models.CharField(max_length=200, verbose_name='Предстоящие сборы')),
                ('pass_info', models.CharField(max_length=200, verbose_name='Прошедшие сборы')),
                ('photo', models.ImageField(upload_to='media/%y/%m/%d/', verbose_name='Фотки о предстоящих сборах')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news', models.TextField(verbose_name='Новости')),
                ('data_publish', models.DateField(verbose_name='Дата публикации')),
            ],
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instagram', models.CharField(max_length=500)),
                ('youtube', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Treiner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Ф.И.О тренера')),
                ('image', models.ImageField(upload_to='media/%Y/%m/%d/', verbose_name='Фотка Информация о тренере ')),
            ],
        ),
        migrations.CreateModel(
            name='Sportman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Ф.И.О спортсмена')),
                ('reiting', models.IntegerField(verbose_name='Рейтинг')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_ufc.category')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '',
            },
        ),
    ]
