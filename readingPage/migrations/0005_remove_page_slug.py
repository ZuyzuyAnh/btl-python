# Generated by Django 4.2.5 on 2023-10-17 02:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('readingPage', '0004_page_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='slug',
        ),
    ]
