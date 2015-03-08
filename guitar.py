import sys
import time
import pygame

import Adafruit_MPR121.MPR121 as MPR121

cap = MPR121.MPR121()

# default I2C address (0x5A).  On BeagleBone Black will default to I2C bus 0.
if not cap.begin():
    print 'Error initializing MPR121.  Check your wiring!'
    sys.exit(1)

pygame.mixer.pre_init(44100, -16, 12, 512)
pygame.init()

SOUND_MAPPING = {
  0: './1st_String_E.wav',
  1: './2nd_String_B_.wav',
  2: './3rd_String_G.wav',
  3: './4th_String_D.wav',
  4: './5th_String_A.wav',
  5: './6th_String_E.wav',
}

sounds = [0,0,0,0,0,0]

for key,soundfile in SOUND_MAPPING.iteritems():
        sounds[key] =  pygame.mixer.Sound(soundfile)
        sounds[key].set_volume(1);

print 'Press Ctrl-C to quit.'
last_touched = cap.touched()
while True:
    current_touched = cap.touched()
    for i in range(7):
        pin_bit = 1 << i
        if current_touched & pin_bit and not last_touched & pin_bit:
            print '{0} touched!'.format(i)
            if (sounds[i]):
                sounds[i].play()
        if not current_touched & pin_bit and last_touched & pin_bit:
            print '{0} released!'.format(i)
    last_touched = current_touched
    time.sleep(0.1)
