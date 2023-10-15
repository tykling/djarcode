import logging
from .models import Reading
from barcodes.models import Barcode
from utils.buzzer import play_sound
from django.core.exceptions import ValidationError

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
    try:
        barcode, created = Barcode.objects.get_or_create(barcode=data)
        logger.debug(f"Ignoring reading {data} - too short or otherwise invalid")
        barcode.full_clean()
    except ValidationError:
        # barcode invalid, too short/error reading
        return
    reading = Reading.objects.create(barcode=barcode)
    logger.debug(f"Created Reading object with UUID {reading.uuid} for {'new' if created else 'existing'} barcode")

    # add to pad and play feedback sound(s)
    try:
        reading.add_to_pad()
        if barcode.product:
            play_sound("success")
        else:
            play_sound("newproduct")
    except Exception:
        play_sound("error")
