# Generated by Django 3.1.1 on 2020-10-12 14:42

from django.db import migrations

def lier_artiste(apps, schema):
    # On récupère les modèles
    Morceau = apps.get_model('musiques', 'Morceau')
    Artiste = apps.get_model('musiques', 'Artiste')

    def get_artiste_by_nom(nom):
        return Artiste.objects.get(nom=nom)

    for morceau in Morceau.objects.all():
        morceau.interprete = get_artiste_by_nom(morceau.artiste)
        morceau.save()

def annuler_lier_artiste(apps, schema):
    Morceau = apps.get_model('musiques', 'Morceau')
    Artiste = apps.get_model('musiques', 'Artiste')

    for morceau in Morceau.objects.all():
        morceau.interprete = null
        morceau.save()

class Migration(migrations.Migration):

    dependencies = [
        ('musiques', '0006_auto_20201012_1623'),
    ]

    operations = [
         migrations.RunPython(lier_artiste,
                             reverse_code=annuler_lier_artiste)
    ]
