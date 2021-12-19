import dialog as dialog
from metadata import metadata
from PIL import Image
import tkinter as tk
import io,os
import pygame, sys
from xspf_lib import Playlist


"""

"""
mainClock = pygame.time.Clock()

pygame.init()
bigfont = pygame.font.SysFont(None, 50)
smallfont = pygame.font.SysFont(None,35)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def PlayListScreen(screen):
    '''
        lors de l'appel de cette fonction depuis le menu principale => choix de la playliste => ouvre une fenetre avec des information sur le contenu de la playlist choisi
    param:screen c'est la fenetre principale sur la quelle on ouvre cette fenetre (Généralement notre MENU)
    '''
    running = True
    path_pl=dialog.getFilePL()#ouvre une boite de dialog pour choisir la playlist XSPF a utiliser
    playlist = Playlist.parse(path_pl)#parse la playlist choisi et extrait tout ses information
    nb_son = playlist.trackList.__len__() #recupere le nombre de son dans la playliste
    #print(nb_son)
    screen = pygame.display.set_mode((750, nb_son*100+100),0,32)#redimensiner le screen suivant le nombre de son dans la playlist
    font =pygame.font.SysFont(None,21)
    while running:
        screen.fill((0,0,0))
        #affichage des texte dans la fenetre dans les metadonne
        draw_text('"ESCAPE" pour revenir au menu',font, (255, 128, 128), screen, 20, 20)
        draw_text('Contenu de la playliste: ', bigfont, (255, 255, 255), screen, 20, 45)
        draw_text(playlist.title, smallfont, (231, 70, 1), screen, 420, 50)#titre de la playlist

        pos = 90
        for son in playlist.trackList:#pour chaque maurceau on affiche son titre son album et sa location
            draw_text('Titre:', smallfont, (121, 248, 248), screen, 20, pos)
            draw_text(son.title, font, (255, 255, 255), screen, 90, pos+5)
            draw_text('Album:', smallfont, (121, 248, 248), screen, 20, pos+25)
            draw_text(son.album, font, (255, 255, 255), screen, 115, pos+30)
            draw_text('localisation:', smallfont, (121, 248, 248), screen, 20, pos+50)
            draw_text(str(son.location), font, (255, 255, 255), screen, 170, pos+55)
            pos+=100#100 px entgre chaque maurceau


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        pygame.display.update()
        mainClock.tick(60)
    screen=pygame.display.set_mode((500,600),0,32)#en redimensionne le screen avec les dimention principaux avant de quité