# Generated by Django 3.1.4 on 2020-12-12 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carwash', '0003_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.CharField(max_length=100)),
            ],
        ),
    ]
