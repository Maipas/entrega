# Generated by Django 4.0.4 on 2022-06-06 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docentes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docente',
            name='nacimiento',
            field=models.DateField(),
        ),
    ]