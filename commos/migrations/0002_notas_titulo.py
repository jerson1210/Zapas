# Generated by Django 4.2.7 on 2023-11-30 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notas',
            name='titulo',
            field=models.CharField(default='Sin título', max_length=255),
        ),
    ]