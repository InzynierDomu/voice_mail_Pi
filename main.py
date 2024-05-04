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
def read_config_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if ':' in line:
                    key, value = line.strip().split(':', 1)
                    globals()[key.strip()] = value.strip()
    except Exception as e:
        print("Error:", e)

# Wywołanie funkcji z nazwą pliku konfiguracyjnego
read_config_file("config.txt")

def write_log(log)
    with open('log.txt', 'w') as file:
        file.write(log)

audio_status = subprocess.run(
    ['arecord', '-l'], capture_output=True, text=True)
if audio_status.returncode == 0:
    write_log(audio_status.stdout)
else:
    write_log("error with audio card")

while True:
    GPIO.output(led_pin, GPIO.LOW)
    GPIO.wait_for_edge(button_pin, GPIO.RISING)
    time.sleep(2)
    if GPIO.input(button_pin) == GPIO.HIGH:
        pygame.init()
        try:
            pygame.mixer.music.load(nazwa_pliku_z_powitaniem)
        except:
            write_log("błędna ściezka do pliku z powitaniem")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
        try:
            pygame.mixer.music.load(nazwa_pliku_z_sygnalem)
        except:
            write_log("błędna ściezka do pliku z sygnałem")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
        pygame.quit()
        GPIO.output(led_pin, GPIO.HIGH)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = timestamp + ".wav"
        process = subprocess.Popen(
            ["arecord", "-D", "plughw:1,0", "--duration=360", "--format=cd", filename])
        GPIO.wait_for_edge(button_pin, GPIO.FALLING)
        process.terminate()