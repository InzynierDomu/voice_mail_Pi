import subprocess
import re
import time
import pygame
from datetime import datetime
import RPi.GPIO as GPIO

button_pin = 23
led_pin = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(led_pin, GPIO.OUT, initial=GPIO.LOW)
def read_config_file(filename):
    config_dict = {}
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if ':' in line:
                    key, value = line.strip().split(':', 1)
                    config_dict[key.strip()] = value.strip()
    except Exception as e:
        print("Error:", e)
    return config_dict

def write_log(log):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('log.txt', 'a') as file:
        file.write(f'{timestamp}: {log}\n')

config = read_config_file("config.txt")
welcome_record_path = config.get('welcome_record_path')
signal_record_path = config.get('signal_record_path')

card_pattern = r"card (\d+):"
subdevice_pattern = r"Subdevice #(\d+):"
output = subprocess.check_output(["arecord", "-l"])
card_match = re.search(card_pattern, output.decode('utf-8'))
subdevice_match = re.search(subdevice_pattern, output.decode('utf-8'))

if card_match and subdevice_match:
    # Extract card and subdevice values from the matches
    card = int(card_match.group(1))
    subdevice = int(subdevice_match.group(1))

    print("Card:", card)
    print("Subdevice:", subdevice)
else:
    write_log("Unable to extract card and subdevice values.")

while True:
    GPIO.output(led_pin, GPIO.LOW)
    GPIO.wait_for_edge(button_pin, GPIO.RISING)
    time.sleep(2)
    if GPIO.input(button_pin) == GPIO.HIGH:
        pygame.init()
        try:
            pygame.mixer.music.load(welcome_record_path)
        except:
            write_log("incorrect path to the welcome record")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
        try:
            pygame.mixer.music.load(signal_record_path)
        except:
            write_log("incorrect path to the signal record")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
        pygame.quit()
        GPIO.output(led_pin, GPIO.HIGH)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = timestamp + ".wav"
        plughw_string = f"plughw:{card},{subdevice}"
        process = subprocess.Popen([
            "arecord",
            "-D",
            plughw_string,
            "--duration=360",
            "--format=cd",
            filename
        ])
        GPIO.wait_for_edge(button_pin, GPIO.FALLING)
        process.terminate()
