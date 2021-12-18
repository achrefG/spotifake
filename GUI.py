# Setup Python ----------------------------------------------- #
import pygame, sys
from playsond import playsond
import dilog
from metadata import metadata
from parcours_directory import parcour_directory
from Creatplaylist import  XspfPlaylist,RecupSong
import tkinter as tk
from tkinter import simpledialog

# Setup pygame/window ---------------------------------------- #


mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('SPOTIFAKE')
pygame.display.set_icon(pygame.image.load("spotifake.png"))
screen = pygame.display.set_mode((600, 600),0,32)

font = pygame.font.SysFont(None, 50)
 # defining a font
smallfont = pygame.font.SysFont(None,35)
# rendering a text written in
# this font
# white color
color = (255,255,255)

txtPlaySond = smallfont.render('Play sond' , True , color)
txtMetadata = smallfont.render('Extraction de metadonne' , True , color)
txtPlayListe = smallfont.render('Playlist par défaut d’un répertoire' , True , color)
txtPlayListe1 = smallfont.render('Playlist avec les morceaux sélectionne ' , True , color)
txtQuit = smallfont.render('Quitter' , True , color)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 


def main_menu():#fenetre principale avec le menu
    click = False
    while True:
        screen.fill((0,0,0))
        draw_text('MENU', font, (255, 255, 255), screen, 20, 20)

        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(50, 100, 500, 50) # appuis => ouvre la fenetre de l'ancien gui

        button_2 = pygame.Rect(50, 200, 500, 50) # appuis => ouvre une fenetre pour l'affichage des metadonne
        
        button_3 = pygame.Rect(50, 300, 500, 50) #  appuis => création d'une playlist depuis un dossier et ses sous fichier

        button_4 = pygame.Rect(50, 400, 500, 50) #  appuis => création d'une playlist a partir des fichier séléctionner

        button_5 = pygame.Rect(50, 500, 500, 50) #  appuis => quitter l'IHM
        if button_1.collidepoint((mx, my)):
            if click:
                path_son=dilog.getFile()
                playsond(path_son)

        if button_2.collidepoint((mx, my)):
            if click:
                metadataScreen()
        
        if button_3.collidepoint((mx, my)):
            if click:
                path=dilog.getDir()
                liste_abspath= parcour_directory(path)
                liste_abspath_musique = RecupSong(liste_abspath)
                
                TitrePlay=None
                while TitrePlay==None:
                    print("ERREUR VOUS N'AVEZ RIEN ENTRE")
                    TitrePlay = simpledialog.askstring("Titre", "entrer un Titre pour votre playlist")

                AuteurPlay=None
                while AuteurPlay==None:
                    print("ERREUR VOUS N'AVEZ RIEN ENTRE")
                    AuteurPlay = simpledialog.askstring("Auteur", "entrer l'Auteur de cette playlist")
                
                XspfPlaylist(TitrePlay,str(AuteurPlay),liste_abspath_musique)

        if button_4.collidepoint((mx, my)):
            if click:
                liste_abspath_musique=dilog.getFiles()

                TitrePlay=None
                while TitrePlay==None:
                    print("ERREUR VOUS N'AVEZ RIEN ENTRE")
                    TitrePlay = simpledialog.askstring("Titre", "entrer un Titre pour votre playlist")

                AuteurPlay=None
                while AuteurPlay==None:
                    print("ERREUR VOUS N'AVEZ RIEN ENTRE")
                    AuteurPlay = simpledialog.askstring("Auteur", "entrer l'Auteur de cette playlist")
                XspfPlaylist(TitrePlay,AuteurPlay,liste_abspath_musique)

        if button_5.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()


        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
        pygame.draw.rect(screen, (255, 0, 0), button_3)
        pygame.draw.rect(screen, (255, 0, 0), button_4)
        pygame.draw.rect(screen, (255, 0, 0), button_5)


        screen.blit(txtPlaySond , (70,110))
        screen.blit(txtMetadata , (70,210))
        screen.blit(txtPlayListe , (70,310))
        screen.blit(txtPlayListe1 , (70,410))
        screen.blit(txtQuit , (70,510))


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
    meta = metadata(path_son,False)
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
                    print("Le fichier METADATA_"+meta.title+".TXT avec les metadonnées viens d'etre créé.")
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
 
#main_menu()
