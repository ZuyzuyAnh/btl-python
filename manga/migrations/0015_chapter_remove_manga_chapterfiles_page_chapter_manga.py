# Generated by Django 4.2.5 on 2023-10-01 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0014_delete_chapters_delete_page_manga_chapterfiles'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter', models.IntegerField(default=0)),
                ('numberOfPages', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='manga',
            name='chapterfiles',
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pageNumber', models.IntegerField(default=0)),
                ('img', models.ImageField(blank=True, null=True, upload_to='manga_images')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='page', to='manga.chapter')),
            ],
        ),
        migrations.AddField(
            model_name='chapter',
            name='manga',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chapter', to='manga.manga'),
        ),
    ]
