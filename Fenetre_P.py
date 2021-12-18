# Setup Python ----------------------------------------------- #
import pygame, sys
import tkinter as tk
from tkinter import simpledialog
import GUI

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('SPOTIFAKE')
pygame.display.set_icon(pygame.image.load("spotifake.png"))
screen = pygame.display.set_mode((600, 600),0,32)

Titlefont = pygame.font.SysFont(None, 75)

smallfont = pygame.font.SysFont(None,45)

color = (0,0,0)

txtPlaySond = smallfont.render('LANCER' , True , color)
txtQuit = smallfont.render('QUITTER' , True , color)

def draw_text(text, Titlefont, color, surface, x, y):
    textobj = Titlefont.render(text, 0, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False

def main():#fenetre principale avec le menu
    # create a surface object, image is drawn on it.
    image = pygame.image.load(r"spotifake.png")
    while True:
        screen.fill((0,0,0))
        draw_text('SPOTIFAKE', Titlefont, (255, 255, 255), screen, 150, 20)
        screen.blit(image, (220, 150))
        mx, my = pygame.mouse.get_pos()

        button_lancer = pygame.Rect(35, 400, 530, 50) #  appuis => création d'une playlist a partir des fichier séléctionner
        button_quit = pygame.Rect(35, 500, 530, 50) #  appuis => quitter l'IHM
        
        if button_lancer.collidepoint((mx, my)):
            if click:
                print("fenetre principale lancer")
                GUI.main_menu()

        
        if button_quit.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()


        pygame.draw.rect(screen, (228, 40, 160), button_lancer)
        pygame.draw.rect(screen, (228, 40, 160), button_quit)



        screen.blit(txtPlaySond , (225,410))
        screen.blit(txtQuit , (220,510))


        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)



 
main()
