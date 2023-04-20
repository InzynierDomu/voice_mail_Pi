import subprocess
import datetime
import RPi.GPIO as GPIO

button_pin = 17
led_pin = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led_pin, GPIO.OUT, initial=GPIO.LOW)

GPIO.output(led_pin, GPIO.HIGH)

while True:
    # zmienic na sprawdzenie zbocza narastajacego
    if GPIO.input(button_pin):
        subprocess.Popen(["aplay", "voice_mail_greetings.wav"])
        GPIO.output(led_pin, GPIO.HIGH)
        now = datetime.datetime.now()
        date_time = now.strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f"nagranie_{date_time}.wav"
        process = subprocess.Popen(["arecord", "-D", "plughw:1,0", "--duration=60", "--format=cd", file_name])
        GPIO.output(led_pin, GPIO.LOW)

    #sprawdzenie czy zostało przerwane
    #GPIO.output(led_pin, GPIO.LOW)
    #process.terminate()