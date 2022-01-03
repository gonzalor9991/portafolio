# Generated by Django 4.0 on 2022-01-03 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_card_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='src',
        ),
        migrations.AddField(
            model_name='card',
            name='imagen',
            field=models.ImageField(default=1, upload_to='Cards', verbose_name='Imagen'),
            preserve_default=False,
        ),
    ]
