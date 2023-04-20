import subprocess
import RPi.GPIO as GPIO

button_pin = 17
led_pin = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led_pin, GPIO.OUT, initial=GPIO.LOW)

GPIO.output(led_pin, GPIO.HIGH)

while True:
    # Oczekiwanie na naciśnięcie przycisku
    if GPIO.input(button_pin):
        subprocess.Popen(["aplay", "test.wav"])
        GPIO.output(led_pin, GPIO.HIGH)
        process = subprocess.Popen(["arecord", "-D", "plughw:1,0", "--duration=60", "--format=cd", "test.wav"])

    #sprawdzenie czy zostało przerwane
    #GPIO.output(led_pin, GPIO.LOW)
    #process.terminate()