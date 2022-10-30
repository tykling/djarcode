import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("djarcode.%s" % __name__)


def do_work():
    """
    The barcode_reader worker runs a keyboard input prompt in a loop and
    creates Reading objects for every enter-terminated input.
    """

    while True:
        reading = Reading(barcode=input("Barcode: "))
        print(f"Created Reading object with UUID {reading.uuid}")
