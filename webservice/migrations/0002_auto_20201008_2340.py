# Generated by Django 2.2.7 on 2020-10-09 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='losbuenosprecios/productos_imagenes/'),
        ),
    ]