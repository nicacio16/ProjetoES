# Generated by Django 3.2.7 on 2021-09-11 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campo',
            name='arquivo',
            field=models.ImageField(upload_to='cars'),
        ),
    ]
