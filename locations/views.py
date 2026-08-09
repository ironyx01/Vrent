from rest_framework import viewsets, permissions
from .models import Bien, Locataire, Paiement
from .serializers import BienSerializer, LocataireSerializer, PaiementSerializer


class BienViewSet(viewsets.ModelViewSet):
    serializer_class = BienSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Bien.objects.filter(proprietaire=self.request.user)

    def perform_create(self, serializer):
        serializer.save(proprietaire=self.request.user)


class LocataireViewSet(viewsets.ModelViewSet):
    serializer_class = LocataireSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Locataire.objects.filter(bien__proprietaire=self.request.user)


class PaiementViewSet(viewsets.ModelViewSet):
    serializer_class = PaiementSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Paiement.objects.filter(locataire__bien__proprietaire=self.request.user)