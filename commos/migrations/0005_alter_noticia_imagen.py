# Generated by Django 4.2.7 on 2023-12-05 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commos', '0004_alter_noticia_imagen_alter_noticia_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='imagen',
            field=models.FileField(upload_to='noticias/'),
        ),
    ]
