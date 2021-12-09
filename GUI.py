#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
import pygame, sys
from playsond import playsond
import dilog
from metadata import metadata
from parcours_directory import parcour_directory
from Creatplaylist import VerifExtension, VerifMime, XspfPlaylist,RecupSong
import tkinter as tk
from tkinter import simpledialog

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((600, 600),0,32)

font = pygame.font.SysFont(None, 25)
 # defining a font
smallfont = pygame.font.SysFont('Corbel',35)
# rendering a text written in
# this font
# white color
color = (255,255,255)

txtPlaySond = smallfont.render('Play sond' , True , color)
txtMetadata = smallfont.render('Extraction de metadonne' , True , color)
txtPlayListe = smallfont.render('Playlist par défaut d’un répertoire' , True , color)
txtPlayListe1 = smallfont.render('Playlist avec les morceaux sélectionne ' , True , color)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False
 
def main_menu():#fenetre principale avec le menu
    while True:
        screen.fill((0,0,0))
        draw_text('main menu', font, (255, 255, 255), screen, 20, 20)

        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(50, 100, 500, 50) # appuis => ouvre la fenetre de l'ancien gui

        button_2 = pygame.Rect(50, 200, 500, 50) # appuis => ouvre une fenetre pour l'affichage des metadonne
        
        button_3 = pygame.Rect(50, 300, 500, 50) #  appuis => création d'une playlist depuis un dossier et ses sous fichier

        button_4 = pygame.Rect(50, 400, 500, 50) #  appuis => création d'une playlist a partir des fichier séléctionner

        if button_1.collidepoint((mx, my)):
            if click:
                path_son=dilog.getFile()
                path_cover="Picture/?.png"
                playsond(path_son,path_cover)


        if button_2.collidepoint((mx, my)):
            if click:
                metadataScreen()
        
        if button_3.collidepoint((mx, my)):
            if click:
                path=dilog.getDir()
                liste_abspath= parcour_directory(path)
                liste_abspath_musique = RecupSong(liste_abspath)
                TitrePlay = simpledialog.askstring("Titre", "entrer un Titre pour votre play liste")
                AuteurPlay = simpledialog.askstring("Auteur", "entrer l'Auteur de cette play liste")
                XspfPlaylist(TitrePlay,AuteurPlay,liste_abspath_musique)

        if button_4.collidepoint((mx, my)):
            if click:
                liste_abspath_musique=dilog.getFiles()
                TitrePlay = simpledialog.askstring("Titre", "entrer un Titre pour votre play liste")
                AuteurPlay = simpledialog.askstring("Auteur", "entrer l'Auteur de cette play liste")
                XspfPlaylist(TitrePlay,AuteurPlay,liste_abspath_musique)
                

        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
        pygame.draw.rect(screen, (255, 0, 0), button_3)
        pygame.draw.rect(screen, (255, 0, 0), button_4)
        
        screen.blit(txtPlaySond , (75,110))
        screen.blit(txtMetadata , (75,210))
        screen.blit(txtPlayListe , (75,310))
        screen.blit(txtPlayListe1 , (75,410))

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


def metadataScreen():#lors de l'appel de cette fonction depuis le menu principale => choix du fichier => une fenetre avec les metadonne
    running = True
    path_son=dilog.getFile()
    meta = metadata(path_son)
    while running:
        screen.fill((0,0,0))
        '''
        affichage des texte dans la fenetre dans les metadonne
        '''
        draw_text('metadata of the chosing file : ', smallfont, (255, 255, 255), screen, 20, 20)
        draw_text(path_son, font, (231, 62, 1), screen, 20, 45)
        
        draw_text('Artist:', smallfont, (121, 248, 248), screen, 40, 100)
        draw_text(meta.artist, font, (255, 255, 255), screen, 140, 105)
        
        draw_text('Album:', smallfont, (121, 248, 248), screen, 40, 140)
        draw_text(meta.album, font, (255, 255, 255), screen, 140, 145)
        
        draw_text('Title:', smallfont, (121, 248, 248), screen, 40, 180)
        draw_text(meta.title, font, (255, 255, 255), screen, 140, 185)
        
        draw_text('duration(secs):', smallfont, (121, 248, 248), screen, 40, 220)
        draw_text(str(meta.duration), font, (255, 255, 255), screen, 220, 225)
        
        draw_text('Musique N°:', smallfont, (121, 248, 248), screen, 40, 260)
        draw_text(meta.track, font, (255, 255, 255), screen, 195, 265)

        draw_text('Compositeur:', smallfont, (121, 248, 248), screen, 40, 300)
        draw_text(meta.composer, font, (255, 255, 255), screen, 210, 305)
        
        draw_text('Genre:', smallfont, (121, 248, 248), screen, 40, 340)
        draw_text(meta.genre, font, (255, 255, 255), screen, 140, 345)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_s:#enregistrer les metadonne dans un fichier txt en appuiant sur s
                    TitreFichier="METADATA_"+meta.title+'.txt'
                    file = open(TitreFichier, "x")
                    file.write("creator  :"+str(meta.artist)+"\n")
                    file.write("title    :"+str(meta.title)+"\n")
                    file.write("duration :"+str(int(meta.duration))+"\n")
                    file.write("album    :"+ str(meta.album) +"\n")  
                    file.write("genre    :"+ str(meta.genre) +"\n")   
                    file.write("composer :"+ str(meta.composer) +"\n")  
                    file.close()
        pygame.display.update()
        mainClock.tick(60)
 
main_menu()
