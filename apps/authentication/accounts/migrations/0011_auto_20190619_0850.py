# Generated by Django 2.2.2 on 2019-06-19 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20190619_0847'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='babysitter',
            new_name='is_babysitter',
        ),
    ]
