# Generated by Django 4.1.3 on 2022-12-11 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0012_delete_answer_delete_question'),
        ('news', '0005_alter_news_created_at_alter_news_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='files',
            field=models.ManyToManyField(blank=True, related_name='news', to='root.file', verbose_name='files'),
        ),
    ]
