# Generated by Django 3.1.7 on 2021-04-12 05:42

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_alter_place_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
    ]