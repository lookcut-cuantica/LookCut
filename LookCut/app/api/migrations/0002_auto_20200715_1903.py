# Generated by Django 3.0.8 on 2020-07-16 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='descripcion',
            field=models.TextField(default='Un corte clásico'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='turno',
            name='fecha',
            field=models.DateField(default="2020-07-16"),
            preserve_default=False,
        ),
    ]