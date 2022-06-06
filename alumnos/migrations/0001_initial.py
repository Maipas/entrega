# Generated by Django 4.0.4 on 2022-06-06 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('nacimiento', models.IntegerField()),
                ('edad', models.IntegerField()),
                ('matricula', models.CharField(max_length=30, unique=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
