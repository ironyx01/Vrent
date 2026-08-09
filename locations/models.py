from django.db import models
from django.contrib.auth.models import User


class Bien(models.Model):
    proprietaire = models.ForeignKey(User, on_delete=models.CASCADE, related_name='biens')
    adresse = models.CharField(max_length=255)
    code_postal = models.CharField(max_length=10)
    ville = models.CharField(max_length=100)
    informations_supplementaires = models.TextField(blank=True)
    loyer_mensuel = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.adresse}, {self.ville}"


class Locataire(models.Model):
    bien = models.ForeignKey(Bien, on_delete=models.CASCADE, related_name='locataires')
    nom = models.CharField(max_length=100)
    date_entree = models.DateField()

    def __str__(self):
        return self.nom


class Paiement(models.Model):
    STATUT_CHOICES = [
        ('paye', 'Payé'),
        ('retard', 'En retard'),
        ('partiel', 'Partiel'),
    ]

    locataire = models.ForeignKey(Locataire, on_delete=models.CASCADE, related_name='paiements')
    mois = models.DateField(help_text="Utiliser le 1er jour du mois, ex: 2026-08-01")
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    statut = models.CharField(max_length=10, choices=STATUT_CHOICES, default='retard')

    class Meta:
        unique_together = ('locataire', 'mois')  # un seul paiement par locataire et par mois

    def __str__(self):
        return f"{self.locataire} - {self.mois} - {self.statut}"