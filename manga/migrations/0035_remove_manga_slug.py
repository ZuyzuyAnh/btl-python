# Generated by Django 4.2.6 on 2023-10-23 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0034_manga_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manga',
            name='slug',
        ),
    ]