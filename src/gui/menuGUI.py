# Setup Python ----------------------------------------------- #
import os
import pygame, sys

from pygame import display
from playsond import playsond
import dialog as dialog
from PIL import Image
from metadata import metadata
from parcours_directory import parcour_directory
from Creatplaylist import  XspfPlaylist,RecupSong
import tkinter as tk
from tkinter import simpledialog
from metadataUI import draw_text, metadataScreen
from readPlayListGUI import PlayListScreen
# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('SPOTIFAKE')
pygame.display.set_icon(pygame.image.load("spotifake.png"))
screen = pygame.display.set_mode((500, 600),0,32)

font = pygame.font.SysFont(None, 50)
 # defining a font
smallfont = pygame.font.SysFont(None,35)
# rendering a text written in
# this font
# white color
color = (255,255,255)
path_cover="spotifake.png"
txtPlaySond = smallfont.render('Jouer un morceau' , True , color)
txtMetadata = smallfont.render('Extraction de metadonne' , True , color)
txtPlayListe = smallfont.render('Playlist par répertoire' , True , color)
txtPlayListe1 = smallfont.render('Playlist personalisée ' , True , color)
txtPlayListe2 = smallfont.render("Contenue d'une Playlist" , True , color)
txtQuit = smallfont.render('Quitter' , True , color)


 


def main_menu():
    '''
        fonction qui lance une fenetre avec le menu des opération qu'on peut effectuer sur notre GUI
    '''
    #fenetre principale avec le menu
    click = False
    running = True
    while running:
        screen.fill((0,0,0))
        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(50, 30, 400, 50) # appuis => ouvre la fenetre de l'ancien gui

        button_2 = pygame.Rect(50, 130, 400, 50) # appuis => ouvre une fenetre pour l'affichage des metadonne
        
        button_3 = pygame.Rect(50, 230, 400, 50) #  appuis => création d'une playlist depuis un dossier et ses sous fichier

        button_4 = pygame.Rect(50, 330, 400, 50) #  appuis => création d'une playlist a partir des fichier séléctionner

        button_5 = pygame.Rect(50, 430, 400, 50) #  appuis => affichier le contenue d'une playlist xspf

        button_6 = pygame.Rect(50, 530, 400, 50) #  appuis => quitter l'IHM

        if button_1.collidepoint((mx, my)):
            if click:
                path_son=dialog.getFile()
                playsond(path_son)

        if button_2.collidepoint((mx, my)):
            if click:
                metadataScreen(screen)
        
        if button_3.collidepoint((mx, my)):
            if click:
                path=dialog.getDir()#return un repertoir
                liste_abspath= parcour_directory(path)#liste des chemin des fichier mp3/flac
                liste_abspath_musique = RecupSong(liste_abspath)#liste des chemin des fichier mp3 avec vérification du type mime
                
                TitrePlay=None
                while TitrePlay==None:#demander a l'utilisateur un titre a la playliste et tourne jusqu'a ce que l'utilisateur en entre un
                    print("ERREUR VOUS N'AVEZ RIEN ENTRE")
                    TitrePlay = simpledialog.askstring("Titre", "entrer un Titre pour votre playlist")

                AuteurPlay=None#demander a l'utilisateur l'auteur de la playliste et tourne jusqu'a ce que l'utilisateur en entre un
                while AuteurPlay==None:
                    print("ERREUR VOUS N'AVEZ RIEN ENTRE")
                    AuteurPlay = simpledialog.askstring("Auteur", "entrer l'Auteur de cette playlist")
                
                XspfPlaylist(TitrePlay,str(AuteurPlay),liste_abspath_musique)#créé une playliste avec les informations récuperer

        if button_4.collidepoint((mx, my)):
            if click:
                liste_abspath_musique=dialog.getFiles()#liste des fichier mp3/flac choisi par l'utilisateur
                TitrePlay=None
                while TitrePlay==None:
                    print("ERREUR VOUS N'AVEZ RIEN ENTRE")
                    TitrePlay = simpledialog.askstring("Titre", "entrer un Titre pour votre playlist")

                AuteurPlay=None
                while AuteurPlay==None:
                    print("ERREUR VOUS N'AVEZ RIEN ENTRE")
                    AuteurPlay = simpledialog.askstring("Auteur", "entrer l'Auteur de cette playlist")
                XspfPlaylist(TitrePlay,AuteurPlay,liste_abspath_musique)#créé une playliste avec les fichiers choisi par l'utilisateur
        if button_5.collidepoint((mx, my)):
            if click:
                PlayListScreen(screen)#ouvre une fenetre avec tout les information sur une playlist choisi par l'utilisateur 
                
        if button_6.collidepoint((mx, my)):#ferme le menu et revien vers la fenetre principale
            if click:
                running = False
                


        pygame.draw.rect(screen, (228, 40, 160), button_1)
        pygame.draw.rect(screen, (228, 40, 160), button_2)
        pygame.draw.rect(screen, (228, 40, 160), button_3)
        pygame.draw.rect(screen, (228, 40, 160), button_4)
        pygame.draw.rect(screen, (228, 40, 160), button_5)
        pygame.draw.rect(screen, (228, 40, 160), button_6)


        screen.blit(txtPlaySond , (70,40))
        screen.blit(txtMetadata , (70,140))
        screen.blit(txtPlayListe , (70,240))
        screen.blit(txtPlayListe1 , (70,340))
        screen.blit(txtPlayListe2 , (70,440))
        screen.blit(txtQuit , (70,540))


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


 
#main_menu()
