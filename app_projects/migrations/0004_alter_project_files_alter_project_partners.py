# Generated by Django 4.1.3 on 2022-12-11 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0012_delete_answer_delete_question'),
        ('projects', '0003_alter_project_files_alter_project_is_finished_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='files',
            field=models.ManyToManyField(blank=True, related_name='projects', to='root.file', verbose_name='files'),
        ),
        migrations.AlterField(
            model_name='project',
            name='partners',
            field=models.ManyToManyField(blank=True, related_name='projects', to='projects.partner', verbose_name='partners'),
        ),
    ]
