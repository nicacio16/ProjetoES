# Generated by Django 3.2.7 on 2021-09-22 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload',
            name='created',
        ),
        migrations.RemoveField(
            model_name='upload',
            name='updated',
        ),
        migrations.AlterField(
            model_name='upload',
            name='action',
            field=models.CharField(choices=[('NO_FILTER', 'no filter'), ('COLORIZED', 'colorized'), ('GRAYSCALE', 'grayscale'), ('BLURRED', 'blurred'), ('BINARY', 'binary'), ('INVERT', 'invert')], help_text='Aqui você coloca um texto', max_length=50, verbose_name='Ação'),
        ),
        migrations.AlterField(
            model_name='upload',
            name='image',
            field=models.ImageField(upload_to='uploads', verbose_name='Imagem'),
        ),
    ]
