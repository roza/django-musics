# Generated by Django 3.1.1 on 2020-10-12 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musiques', '0004_auto_20201012_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='morceau',
            name='interprete',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='morceaux', to='musiques.artiste'),
        ),
    ]