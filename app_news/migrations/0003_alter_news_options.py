# Generated by Django 4.1.3 on 2022-11-28 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_news_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ('created_at',), 'verbose_name': 'news', 'verbose_name_plural': 'news'},
        ),
    ]
