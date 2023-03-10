# Generated by Django 4.1.6 on 2023-02-09 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='')),
                ('phone_num', models.CharField(max_length=20, verbose_name='')),
                ('adress', models.CharField(max_length=50, verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='')),
                ('discription', models.CharField(max_length=200, verbose_name='')),
                ('color', models.CharField(max_length=20, verbose_name='')),
            ],
        ),
    ]
