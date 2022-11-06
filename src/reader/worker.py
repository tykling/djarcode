import logging
from .models import Reading
from barcodes.models import Barcode

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("djarcode.%s" % __name__)


def do_work():
    """
    The barcode_reader worker runs a keyboard input prompt and
    creates Reading objects for every enter-terminated input.
    """
    data = input("Barcode: ")
    if not data:
        return
    barcode, created = Barcode.objects.get_or_create(barcode=data)
    reading = Reading.objects.create(barcode=barcode)
    print(f"Created Reading object with UUID {reading.uuid} for {'new' if created else 'existing'} barcode")
