# Generated by Django 4.0.4 on 2022-06-06 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('nacimiento', models.IntegerField()),
                ('edad', models.IntegerField()),
                ('materia', models.CharField(max_length=30, unique=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
