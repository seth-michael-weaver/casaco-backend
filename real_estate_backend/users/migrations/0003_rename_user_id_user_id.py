# Generated by Django 3.2 on 2023-05-14 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_id_user_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user_id',
            new_name='id',
        ),
    ]