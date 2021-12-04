import pygame, sys, time
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Memes.')

meme = pygame.mixer.Sound('C:/Users/kakif/Desktop/python/projet/Musique/Vanille.mp3')
meme.play()
#time.sleep(2)
#meme.stop()
"""
while True: # Main Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            pygame.display.update()       
    #sys.exit()
"""