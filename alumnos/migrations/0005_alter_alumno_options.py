# Generated by Django 4.0.4 on 2022-07-01 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0004_alter_alumno_nacimiento'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alumno',
            options={'verbose_name': 'alumno', 'verbose_name_plural': 'alumnos'},
        ),
    ]
