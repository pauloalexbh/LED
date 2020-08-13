import board
import RPi.GPIO as gpio
import neopixel
from random import SystemRandom
rand=SystemRandom()
import time

pixels = neopixel.NeoPixel(board.D18, 2)
print("Ligando led 0 em vermelho")
pixels[0] = (255, 0, 0)

while True:
    try:
        R=rand.randrange(256)
        G=rand.randrange(256)
        B=rand.randrange(256)
        print("Mudando a cor do led 0")
        pixels[0] = (R, G, B)
        time.sleep(1)
        
        
        R=rand.randrange(256)
        G=rand.randrange(256)
        B=rand.randrange(256)
        print("Mudando a cor do led 1")
        pixels[1] = (R, G, B)
        time.sleep(1)
        
    except (KeyboardInterrupt):
        print("Saindo")
        gpio.cleanup()
        exit()