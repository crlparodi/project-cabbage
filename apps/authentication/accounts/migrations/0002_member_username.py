# Generated by Django 2.2.2 on 2019-06-15 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounts',
            name='username',
            field=models.CharField(default='BOUH', max_length=255, verbose_name="Nom d'utilisateur"),
        ),
    ]
