import pygame, sys
import tkinter as tk
from tkinter import simpledialog
import menuGUI

mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('SPOTIFAKE')#titre de la fenetre principale
pygame.display.set_icon(pygame.image.load("./spotifake.png"))#mettre notre logo comme icon du logiciel
screen = pygame.display.set_mode((500, 600),0,32)#initialiser la fenetre

Titlefont = pygame.font.SysFont(None, 75)
smallfont = pygame.font.SysFont(None,45)

color = (255,255,255) #WHITE

txtPlaySond = smallfont.render('LANCER' , True , color)
txtQuit = smallfont.render('QUITTER' , True , color)

def draw_text(text, Titlefont, color, surface, x, y):
    '''
    Fonction pour simplifier l'écriture sur une fenetre pygame  
    '''
    textobj = Titlefont.render(text, 0, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 


def main():
    '''
        crée et initialise une fenetre principale avec le logo de notre application et deux button pour lancer ou quiter notre user interface
    '''
    #
    # create a surface object, image is drawn on it.
    image = pygame.image.load(r"spotifake.png")
    click = False
    while True:
        
        screen.fill((0,0,0))
        draw_text('SPOTIFAKE', Titlefont, (255, 255, 255), screen, 100, 20)
        screen.blit(image, (160, 150)) # metre le logo sur 160,150
        mx, my = pygame.mouse.get_pos()

        button_lancer = pygame.Rect(35, 400, 430, 50) #  appuis => lance la fenétre avec le menu principale 
        button_quit = pygame.Rect(35, 500, 430, 50) #  appuis => quitter l'IHM
        
        if button_lancer.collidepoint((mx, my)):
            if click:
                print("fenetre principale lancer")
                menuGUI.main_menu()

        
        if button_quit.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()


        pygame.draw.rect(screen, (228, 40, 160), button_lancer)
        pygame.draw.rect(screen, (228, 40, 160), button_quit)



        screen.blit(txtPlaySond , (180,410))
        screen.blit(txtQuit , (175,510))


        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:#fermer le progromme si la touche Echap et appuier 
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)


main()#lancer notre GUI
