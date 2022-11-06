import uuid
from etherpad_lite import EtherpadLiteClient
from bs4 import BeautifulSoup
from django.db import models
from django.conf import settings


class Reading(models.Model):
    """A reading from the barcode scanner."""
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    barcode = models.ForeignKey("barcodes.Barcode", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.barcode} scanned at {self.created}"

    def add_to_pad(self):
        """Add this reading to the shoppinglist."""
        for req in ["PAD_URL", "PAD_KEY", "PAD_NAME"]:
            if not hasattr(settings, req):
                print(f"missing setting: {req}")
                return
        c = EtherpadLiteClient(base_url=settings.PAD_URL, base_params={'apikey': settings.PAD_KEY})
        soup = BeautifulSoup(c.getHTML(padID=settings.PAD_NAME)["html"], features="html.parser")
        li = soup.new_tag("li")
        li.string = str(self.barcode)
        soup.body.ul.append(li)
        c.setHTML(padID=settings.PAD_NAME, html=str(soup), authorId="djarcode")
