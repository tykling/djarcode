from django.contrib import admin
from .models import Barcode

@admin.register(Barcode)
class BarcodeAdmin(admin.ModelAdmin):
    list_display = ["uuid", "barcode", "created", "product"]
    list_filter = ["product"]
