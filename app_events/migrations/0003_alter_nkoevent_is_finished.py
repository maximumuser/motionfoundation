# Generated by Django 4.1.3 on 2022-11-28 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_nkoevent_alter_address_options_delete_event_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nkoevent',
            name='is_finished',
            field=models.BooleanField(db_index=True, default=False, help_text='Is this event has finished?'),
        ),
    ]
