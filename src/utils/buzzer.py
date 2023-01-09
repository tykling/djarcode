import sys
import RPi.GPIO as GPIO
import time
from django.conf import settings

def play_sound(sound):
    """Play a little bit of sound using PWD with a piezo buzzer on a GPIO port."""
    if not hasattr(settings, "BUZZER_GPIO_PIN"):
        return
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(settings.BUZZER_GPIO_PIN, GPIO.OUT)
    if sound == "newproduct":
        buzzer = GPIO.PWM(settings.BUZZER_GPIO_PIN, 698)
        for _ in range(3):
            buzzer.ChangeFrequency(698)
            buzzer.start(99)
            time.sleep(0.1)
            buzzer.stop()
            time.sleep(0.05)
        buzzer.start(99)
        buzzer.ChangeFrequency(523)
        time.sleep(0.8)
        buzzer.stop()
    elif sound == "error":
        buzzer = GPIO.PWM(settings.BUZZER_GPIO_PIN, 523)
        buzzer.ChangeFrequency(523)
        buzzer.start(99)
        time.sleep(0.2)
        buzzer.stop()
        buzzer.ChangeFrequency(400)
        buzzer.start(99)
        time.sleep(0.2)
        buzzer.stop()
        buzzer.ChangeFrequency(300)
        buzzer.start(99)
        time.sleep(0.2)
        buzzer.stop()
        buzzer.ChangeFrequency(200)
        buzzer.start(99)
        time.sleep(0.7)
        buzzer.stop()
    elif sound == "success":
        buzzer = GPIO.PWM(settings.BUZZER_GPIO_PIN, 523)
        buzzer.ChangeFrequency(650)
        buzzer.start(50)
        time.sleep(0.2)
        buzzer.stop()
        buzzer.start(50)
        buzzer.ChangeFrequency(750)
        time.sleep(0.2)
        buzzer.stop()
    GPIO.cleanup()
