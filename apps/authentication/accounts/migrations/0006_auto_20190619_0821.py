# Generated by Django 2.2.2 on 2019-06-19 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20190619_0809'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='Administrateur'),
        ),
        migrations.AddField(
            model_name='member',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='Staff'),
        ),
    ]
