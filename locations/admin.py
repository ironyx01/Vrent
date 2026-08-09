from django.contrib import admin
from .models import Bien, Locataire, Paiement

admin.site.register(Bien)
admin.site.register(Locataire)
admin.site.register(Paiement)