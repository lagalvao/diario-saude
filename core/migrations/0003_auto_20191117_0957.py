# Generated by Django 2.2.6 on 2019-11-17 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20191117_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historico',
            name='remedio',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='historico',
            name='usuario',
            field=models.IntegerField(),
        ),
    ]
