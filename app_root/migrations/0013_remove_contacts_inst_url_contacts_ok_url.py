# Generated by Django 4.1.3 on 2022-12-12 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0012_delete_answer_delete_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacts',
            name='inst_url',
        ),
        migrations.AddField(
            model_name='contacts',
            name='ok_url',
            field=models.URLField(blank=True, verbose_name='odnoklassniki url'),
        ),
    ]
