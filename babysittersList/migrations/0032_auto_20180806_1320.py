# Generated by Django 2.0.7 on 2018-08-06 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babysittersList', '0031_auto_20180718_1614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
        migrations.AlterField(
            model_name='babysitter',
            name='time_target',
            field=models.CharField(blank=True, choices=[('AM', 'Matin'), ('PM', 'Après-midi'), ('NO', 'Soir'), ('DI', 'Toute la journée')], max_length=4, verbose_name='Moments de la journée'),
        ),
    ]
