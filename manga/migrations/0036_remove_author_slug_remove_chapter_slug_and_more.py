# Generated by Django 4.2.6 on 2023-10-23 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0035_remove_manga_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='chapter',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='slug',
        ),
    ]