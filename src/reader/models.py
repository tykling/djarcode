import uuid

from django.db import models


class Reading(models.Model):
    """A reading from the barcode scanner."""
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    barcode = models.ForeignKey("barcodes.Barcode", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.barcode} scanned at {self.created}"
