# Generated by Django 2.0.7 on 2018-07-17 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babysittersList', '0025_user_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='babysitter',
            name='linkedin',
            field=models.URLField(blank=True, verbose_name='Profil LinkedIn'),
        ),
    ]
