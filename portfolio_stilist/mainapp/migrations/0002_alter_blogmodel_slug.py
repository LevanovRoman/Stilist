# Generated by Django 4.1.2 on 2022-11-21 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='slug',
            field=models.SlugField(max_length=25, unique=True, verbose_name='URL'),
        ),
    ]
