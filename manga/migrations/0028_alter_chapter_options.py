# Generated by Django 4.2.5 on 2023-10-05 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0027_alter_chapter_options_chapter_updated_manga_updated'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chapter',
            options={'ordering': ['name']},
        ),
    ]