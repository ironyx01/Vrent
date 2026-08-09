from rest_framework.routers import DefaultRouter
from .views import BienViewSet, LocataireViewSet, PaiementViewSet

router = DefaultRouter()
router.register(r'biens', BienViewSet, basename='bien')
router.register(r'locataires', LocataireViewSet, basename='locataire')
router.register(r'paiements', PaiementViewSet, basename='paiement')

urlpatterns = router.urls