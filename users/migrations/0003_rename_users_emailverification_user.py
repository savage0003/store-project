# Generated by Django 3.2.22 on 2023-11-11 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20231111_1338'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emailverification',
            old_name='users',
            new_name='user',
        ),
    ]
