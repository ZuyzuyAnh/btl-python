# Generated by Django 4.2.5 on 2023-10-02 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manga', '0021_delete_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manga.chapter')),
            ],
        ),
    ]
