# Generated by Django 3.1.1 on 2020-10-12 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musiques', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='morceau',
            name='date_sortie',
            field=models.DateField(null=True),
        ),
    ]
