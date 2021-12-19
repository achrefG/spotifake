# Setup Python ----------------------------------------------- #
import os
import pygame, sys
from playsond import playsond
import dilog
from PIL import Image
from metadata import metadata
from parcours_directory import parcour_directory
from Creatplaylist import  XspfPlaylist,RecupSong
import tkinter as tk
from tkinter import simpledialog
import io
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
 
        button_1 = pygame.Rect(50, 100, 400, 50) # appuis => ouvre la fenetre de l'ancien gui

        button_2 = pygame.Rect(50, 200, 400, 50) # appuis => ouvre une fenetre pour l'affichage des metadonne
        
        button_3 = pygame.Rect(50, 300, 400, 50) #  appuis => création d'une playlist depuis un dossier et ses sous fichier

        button_4 = pygame.Rect(50, 400, 400, 50) #  appuis => création d'une playlist a partir des fichier séléctionner

        button_5 = pygame.Rect(50, 500, 400, 50) #  appuis => quitter l'IHM
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


        pygame.draw.rect(screen, (228, 40, 160), button_1)
        pygame.draw.rect(screen, (228, 40, 160), button_2)
        pygame.draw.rect(screen, (228, 40, 160), button_3)
        pygame.draw.rect(screen, (228, 40, 160), button_4)
        pygame.draw.rect(screen, (228, 40, 160), button_5)


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

    metafont=pygame.font.SysFont(None,27)
    font =pygame.font.SysFont(None,22)
    while running:
        screen.fill((0,0,0))
        #affichage des texte dans la fenetre dans les metadonne

        draw_text('Metadonnée du fichier : ', smallfont, (255, 255, 255), screen, 20, 20)
        nomfichier=os.path.relpath(path_son) # stockage du chemin relatif du fichier audio selectionné
        draw_text(nomfichier, metafont, (231, 70, 1), screen, 300, 25)
        
        draw_text('Appuyer sur "S" pour sauvgarder les meta données',font, (255, 255, 255), screen, 20, 55)
        draw_text('"ESCAPE" pour revenir au menu',font, (255, 255, 255), screen, 20, 75)
        

        draw_text('Artiste:', smallfont, (121, 248, 248), screen, 20, 110)
        draw_text(meta.artist, metafont, (255, 255, 255), screen, 130, 115)
        
        draw_text('Album:', smallfont, (121, 248, 248), screen, 20, 150)
        draw_text(meta.album, metafont, (255, 255, 255), screen, 130, 155)
        
        draw_text('Titre:', smallfont, (121, 248, 248), screen, 20, 190)
        draw_text(meta.title, metafont, (255, 255, 255), screen, 100, 195)
        
        draw_text('durée(secs):', smallfont, (121, 248, 248), screen, 20, 230)
        draw_text(str(meta.duration), metafont, (255, 255, 255), screen, 210, 235)
        
        draw_text('Musique N°:', smallfont, (121, 248, 248), screen, 20, 270)
        draw_text(meta.track, metafont, (255, 255, 255), screen, 185, 275)

        draw_text('Compositeur:', smallfont, (121, 248, 248), screen, 20, 310)
        draw_text(meta.composer, metafont, (255, 255, 255), screen, 200, 315)
        
        draw_text('Genre:', smallfont, (121, 248, 248), screen, 20, 350)
        draw_text(meta.genre, metafont, (255, 255, 255), screen, 130, 355)
        
        pygame.draw.rect(screen,(121, 248, 248), [210, 420, 170, 170], 10, border_radius=15)
        cover = meta.get_image() # Stockage de la cover sous forme de bytes si elle existe None sinon

        if(cover != None): # si le fichier audio a une cover 
            pi = Image.open(io.BytesIO(cover)) # ouverture de l'image avec PIL (avec conversion des bytes au format img) 
            print("\nLa cover du fichier audio que vous voulez jouer est "+ str(pi.format) + " retrouver la enregister dans Picture\cover."+str(pi.format)+"\n") # test pour connaitre le format de l'image decoder 
            cover = 'Picture\cover.'+str(pi.format) # enregistrement du nom de la cover decodée 'Picture\cover.'+ format de l'image decoder ( png ou jpeg )
            pi.save(cover) # enregistrement de l'image decodée 
        else: # si le fichier audio n'a  pas de cover 
            cover=path_cover  # attribution de la cover par defaut

        image = pygame.image.load(cover)
        image = pygame.transform.scale(image , (150,150)) # redimenssion de l'image a la taille 150.150
        screen.blit(image, (220, 430))

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
 
main_menu()
