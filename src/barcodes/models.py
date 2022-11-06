import uuid
from django.db import models

class Barcode(models.Model):
    """A barcode."""
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    barcode = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.product if self.product else self.barcode