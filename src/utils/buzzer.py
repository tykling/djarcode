import sys
import RPi.GPIO as GPIO
import time
from django.conf import settings

def play_sound():
    """Play a little bit of sound using PWD with a piezo buzzer on a GPIO port."""
    if not hasattr(settings, "BUZZER_GPIO_PIN"):
        return
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(settings.BUZZER_GPIO_PIN, GPIO.OUT)
    buzzer = GPIO.PWM(settings.BUZZER_GPIO_PIN, 698)
    for _ in range(3):
        buzzer.ChangeFrequency(698)
        buzzer.start(50)
        time.sleep(0.2)
        buzzer.stop()
        time.sleep(0.1)
    buzzer.start(50)
    buzzer.ChangeFrequency(523)
    time.sleep(1)
    buzzer.stop()
    GPIO.cleanup()
