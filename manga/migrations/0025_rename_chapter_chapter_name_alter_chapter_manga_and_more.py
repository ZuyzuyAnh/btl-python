# Generated by Django 4.2.5 on 2023-10-04 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0024_remove_chapter_page_remove_manga_chapters_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chapter',
            old_name='chapter',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='chapter',
            name='manga',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='manga', to='manga.manga'),
        ),
        migrations.AlterField(
            model_name='manga',
            name='author',
            field=models.ForeignKey(default='unknown', on_delete=django.db.models.deletion.CASCADE, related_name='author', to='manga.author'),
        ),
    ]
