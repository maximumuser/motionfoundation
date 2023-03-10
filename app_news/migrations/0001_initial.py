# Generated by Django 4.1.3 on 2022-11-24 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('root', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=128, verbose_name='title')),
                ('description', models.TextField(blank=True, max_length=2048, verbose_name='description')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('short_description', models.TextField(blank=True, max_length=512, verbose_name='short description')),
                ('files', models.ManyToManyField(related_name='news', to='root.file')),
            ],
        ),
    ]
