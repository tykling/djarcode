import logging
from .models import Reading

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("djarcode.%s" % __name__)


def do_work():
    """
    The barcode_reader worker runs a keyboard input prompt and
    creates Reading objects for every enter-terminated input.
    """
    reading = Reading(barcode=input("Barcode: "))
    print(f"Created Reading object with UUID {reading.uuid}")
