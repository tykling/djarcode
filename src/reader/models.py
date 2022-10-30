import uuid

from django.db import models


class Reading(models.Model):
    """A reading from the barcode scanner."""

    class Meta:
        abstract = True

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    barcode = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
