from django.contrib import admin
from .models import Reading

@admin.register(Reading)
class ReadingAdmin(admin.ModelAdmin):
    list_display = ["uuid", "barcode", "created"]
