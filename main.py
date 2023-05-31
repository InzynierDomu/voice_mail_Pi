import subprocess
import time
import pygame
from datetime import datetime
import RPi.GPIO as GPIO

button_pin = 1
led_pin = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(led_pin, GPIO.OUT, initial=GPIO.LOW)

audio_status = subprocess.run(
    ['arecord', '-l'], capture_output=True, text=True)
if audio_status.returncode == 0:
    with open('/home/pi/output.txt', 'w') as file:
        file.write(audio_status.stdout)
else:
    with open('/home/pi/output.txt', 'w') as file:
        file.write("error with audio hw")

while True:
    GPIO.output(led_pin, GPIO.LOW)
    GPIO.wait_for_edge(button_pin, GPIO.RISING)
    time.sleep(2)
    if GPIO.input(button_pin) == GPIO.HIGH:
        pygame.init()
        pygame.mixer.music.load("/home/pi/welcome_record.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
        pygame.mixer.music.load("/home/pi/signal.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
        pygame.quit()
        GPIO.output(led_pin, GPIO.HIGH)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = "/home/pi/record_" + timestamp + ".wav"
        process = subprocess.Popen(
            ["arecord", "-D", "plughw:1,0", "--duration=360", "--format=cd", filename])
        GPIO.wait_for_edge(button_pin, GPIO.FALLING)
        process.terminate()
