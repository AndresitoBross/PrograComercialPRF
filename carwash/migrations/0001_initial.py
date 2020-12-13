# Generated by Django 3.1.4 on 2020-12-13 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('dpi', models.CharField(max_length=10)),
                ('telefono', models.CharField(max_length=8)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('Descripcion', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Marcas',
            },
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=50)),
                ('precio', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Servicios',
            },
        ),
        migrations.CreateModel(
            name='Automovil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carwash.cliente')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carwash.marca')),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carwash.servicio')),
            ],
            options={
                'verbose_name_plural': 'Automoviles',
            },
        ),
    ]
