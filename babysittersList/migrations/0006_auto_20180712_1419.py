# Generated by Django 2.0.7 on 2018-07-12 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babysittersList', '0005_auto_20180711_2011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='babysitter',
            name='Nom',
        ),
        migrations.AddField(
            model_name='babysitter',
            name='nurse_name',
            field=models.CharField(default=' ', max_length=42),
        ),
    ]