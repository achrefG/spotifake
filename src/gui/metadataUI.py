import dialog as dialog
from metadata import metadata
from PIL import Image
import tkinter as tk
import io,os
import pygame, sys
mainClock = pygame.time.Clock()
path_cover="spotifake.png"
pygame.init()
font = pygame.font.SysFont(None, 50)
 # defining a font
smallfont = pygame.font.SysFont(None,35)
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def metadataScreen(screen):
    '''
        lors de l'appel de cette fonction depuis le menu principale => choix du fichier => une fenetre avec les metadonne
    param: la fenetre principal sur la quelle on ouvre cette fenetre (dans notre GUI c'est La fenetre MENU)

    '''
    running = True
    path_son=dialog.getFile()#ouvre une boite de dialog pour choisir un fichier (mp3/flac)
    meta = metadata(path_son,False)#recupere les metadonne du fichier choisi

    metafont=pygame.font.SysFont(None,27)
    font =pygame.font.SysFont(None,21)
    cover = meta.get_image() # Stockage de la cover sous forme de bytes si elle existe None sinon
    if(cover != None): # si le fichier audio a une cover 
        pi = Image.open(io.BytesIO(cover)) # ouverture de l'image avec PIL (avec conversion des bytes au format img) 
        print("\nLa cover du fichier audio que vous voulez jouer est "+ str(pi.format) + " retrouver la enregister dans Picture\cover."+str(pi.format)+"\n") # test pour connaitre le format de l'image decoder 
        cover = 'Picture\cover.'+str(pi.format) # enregistrement du nom de la cover decodée 'Picture\cover.'+ format de l'image decoder ( png ou jpeg )
        pi.save(cover) # enregistrement de l'image decodée 
    else: # si le fichier audio n'a  pas de cover 
        cover=path_cover  # attribution de la cover par defaut

    while running:
        screen.fill((0,0,0))
        #affichage des texte dans la fenetre dans les metadonne
        
        draw_text('Appuyer sur "S" pour sauvgarder les meta données',font, (255, 128, 128), screen, 20, 20)
        draw_text('"ESCAPE" pour revenir au menu',font, (255, 128, 128), screen, 20, 40)
        


        draw_text('Metadonnée du fichier : ', smallfont, (255, 255, 255), screen, 20, 70)
        nomfichier=os.path.basename(path_son) # stockage du chemin relatif du fichier audio selectionné
        draw_text(nomfichier, metafont, (231, 70, 1), screen, 175, 95)


        draw_text('Artiste:', smallfont, (121, 248, 248), screen, 20, 110)#afichier l'artiste du son
        draw_text(meta.artist, metafont, (255, 255, 255), screen, 130, 115)
        
        draw_text('Album:', smallfont, (121, 248, 248), screen, 20, 150)#afichier l'Album du son
        draw_text(meta.album, metafont, (255, 255, 255), screen, 130, 155)
        
        draw_text('Titre:', smallfont, (121, 248, 248), screen, 20, 190)#afichier le Titre du son
        draw_text(meta.title, metafont, (255, 255, 255), screen, 100, 195)
        
        draw_text('durée(secs):', smallfont, (121, 248, 248), screen, 20, 230)#afichier la durée en secs du son
        draw_text(str(meta.duration), metafont, (255, 255, 255), screen, 175, 235)
        
        draw_text('Musique N°:', smallfont, (121, 248, 248), screen, 20, 270)#afichier le numéro du son
        draw_text(meta.track, metafont, (255, 255, 255), screen, 185, 275)

        draw_text('Compositeur:', smallfont, (121, 248, 248), screen, 20, 310)#afichier le Compositeur du son
        draw_text(meta.composer, metafont, (255, 255, 255), screen, 200, 315)
        
        draw_text('Genre:', smallfont, (121, 248, 248), screen, 20, 350)#afichier le Genre du son
        draw_text(meta.genre, metafont, (255, 255, 255), screen, 130, 355)
        
        pygame.draw.rect(screen,(121, 248, 248), [165, 420, 170, 170], 10, border_radius=15)#mettre un cadre pour le cover du son




        image = pygame.image.load(cover)#init le cover
        image = pygame.transform.scale(image , (150,150)) # redimenssion de l'image a la taille 150.150
        screen.blit(image, (175, 430))#mettre le cover sur le cadre dans la fenetre

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_s:#enregistrer les metadonne dans un fichier txt en appuiant sur s
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