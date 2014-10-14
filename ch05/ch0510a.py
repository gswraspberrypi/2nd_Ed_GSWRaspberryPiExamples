import pygame
import pygame.midi
from time import sleep

instrument = 0
note = 74
volume = 127

pygame.init()
pygame.midi.init()

#port = pygame.midi.get_default_output_id()
port = 2
print(port)
midiOutput = pygame.midi.Output(port, 0)
midiOutput.set_instrument(instrument)
for note in range(0, 127):
    midiOutput.note_on(note, volume) 
    sleep(.25)
    midiOutput.note_off(note, volume)
del midiOutput
pygame.midi.quit()
