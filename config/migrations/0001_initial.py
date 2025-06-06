# Generated by Django 5.1.7 on 2025-04-01 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos/')),
                ('video_principal', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('imagens', models.ImageField(blank=True, null=True, upload_to='imagens/')),
            ],
        ),
    ]
