# Generated by Django 5.2 on 2025-04-08 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0006_siteconfig_video_viagens'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfig',
            name='imagen_png',
            field=models.ImageField(blank=True, null=True, upload_to='imagens/'),
        ),
    ]
