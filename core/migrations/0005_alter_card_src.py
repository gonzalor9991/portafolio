# Generated by Django 4.0 on 2022-01-03 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_card_imagen_card_src'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='src',
            field=models.CharField(max_length=200, verbose_name='src'),
        ),
    ]
