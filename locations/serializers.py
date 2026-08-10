from rest_framework import serializers
from .models import Bien, Locataire, Paiement


class PaiementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paiement
        fields = ['id', 'locataire', 'mois', 'montant', 'statut']


class LocataireSerializer(serializers.ModelSerializer):
    paiements = PaiementSerializer(many=True, read_only=True)

    class Meta:
        model = Locataire
        fields = ['id', 'bien', 'nom', 'date_entree', 'email', 'telephone', 'garant_nom', 'garant_email', 'garant_telephone', 'paiements']


class BienSerializer(serializers.ModelSerializer):
    locataires = LocataireSerializer(many=True, read_only=True)

    class Meta:
        model = Bien
        fields = ['id', 'adresse', 'code_postal', 'ville', 'informations_supplementaires', 'loyer_mensuel', 'locataires']