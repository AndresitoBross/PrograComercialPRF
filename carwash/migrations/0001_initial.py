<<<<<<< HEAD
# Generated by Django 2.2.17 on 2020-12-12 03:40

from django.db import migrations, models
=======
# Generated by Django 3.1.4 on 2020-12-12 03:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
>>>>>>> master


class Migration(migrations.Migration):

    initial = True

    dependencies = [
<<<<<<< HEAD
=======
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
>>>>>>> master
    ]

    operations = [
        migrations.CreateModel(
<<<<<<< HEAD
            name='Servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.CharField(max_length=100)),
            ],
=======
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('Descripcion', models.TextField()),
                ('marcaid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Marcas',
            },
>>>>>>> master
        ),
    ]
