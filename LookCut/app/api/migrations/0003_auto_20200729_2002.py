# Generated by Django 3.0.5 on 2020-07-29 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200715_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='barbero',
            name='cedula',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='cedula',
            field=models.CharField(default=123456789, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='contraseña',
            field=models.CharField(default='password', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='userName',
            field=models.CharField(default='sarpn', max_length=200),
            preserve_default=False,
        ),
    ]