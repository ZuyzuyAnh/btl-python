# Generated by Django 4.2.5 on 2023-10-04 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0025_rename_chapter_chapter_name_alter_chapter_manga_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chapter',
            options={'ordering': ['name']},
        ),
    ]
