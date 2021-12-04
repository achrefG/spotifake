import pygame
import io
from PIL import Image
from tinytag import TinyTag
from pygame.display import get_caption
from metadata import metadata
def GUI(path_son ,path_cover):
    meta = metadata(path_son)
    cover = meta.get_image()
    if(cover != None):
        pi = Image.open(io.BytesIO(cover))
        print(pi.format)
        cover = 'Picture/cover.'+str(pi.format)
        pi.save(cover)
    else:
        pi=Image.open(path_cover)    
    w,h=pi.size # stockage des dimensions de l'image 
    
    pygame.init() # initialisation de l'objet pygame
    pygame.display.set_caption(" AFFICHE COVER & LIS LE SON ")# Titre de la fenetre
    
    # PRENDRE LA BONNE DIMMENSION // A MODIFIER QUAND INTERFACE GRAPHIQUE SERA EFFECTUEE
    if ((w==h) and (w>800)):
        resolution_fenetre = (500,500) # taille de la fenêtre 
    elif((w!=h and (w>1000 or h>800))):
        resolution_fenetre = (w/2,h/2) # taille de la fenêtre 
    else:
        resolution_fenetre= (w,h)

    surface_fenetre = pygame.display.set_mode(resolution_fenetre) # parametrage de la surface de la fenetre 
    

    son=pygame.mixer.music
    son.load(path_son) # creation de l'objet son grâce au path du fichier donnee en paramêtre
    son.play(0,0,0)
    if(cover != None):    
        son_cover = pygame.image.load(cover) # creation d'un nouvel objet image a partir de l'image en metadonne
    else:
        son_cover = pygame.image.load(path_cover) # creation d'un nouvel objet image a partir d'un fichier donnee en paramêtre

    son_cover = pygame.transform.scale(son_cover , resolution_fenetre) # redimenssion de l'image a la taille de la fenêtre
    son_cover.convert() # conversion du format des pixels en un unique => facilites l'affichage
    #son_cover.set_colorkey((255,255,255)) # sert a rendre transparent(=> PNG ) les pixels de la couleur donnee en parametre 

    surface_fenetre.fill((0,0,0)) # fill : choix de la couleur pour le fond de la fenêtre
    surface_fenetre.blit(son_cover, [0,0]) # blit[0]: nom du fichier image et blit[1]: position du point en haut a gauche de l'image
    pygame.display.flip() # met a jour la fenêtre afficher
    
    pause =False

    lancer = True # boolean qui permet de garder la fenêtre ouverte tant quelle est vrai
    while lancer: # tant que lancer est vrai 
        print(son.get_busy())
        for event in pygame.event.get(): # pour event variant en fonction de ce qu'il ce passe dans la fenêtre 
            if event.type == pygame.QUIT: # si l'evenement est : la fenetre est quitter 
                lancer = False # lancer devient faux et la fenêtre ne tourne plus 
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    if pause==False: #pause avec p
                        son.pause()
                        pause=True 
                    else:# unpause avec p
                        son.unpause()
                        pause=False
                    
                if event.key == pygame.K_r : # replay avec r
                    son.rewind()
                    
                if event.key == pygame.K_UP: # augmente le volume avec la fleche du haut 
                    son.set_volume(son.get_volume()+0.1)
                if event.key == pygame.K_DOWN:
                    son.set_volume(son.get_volume()-0.1)# baisse le volume avec la fleche du bas 
                if event.key == pygame.K_q:#fermer le programme avec q
                   lancer=False
                ''' 
                if event.key == pygame.K_RIGHT:
                    son.set_volume(son.get_pos()-0.1)
                if event.key == pygame.K_RIGHT:
                    son.set_volume(son.get_pos()-0.1)
                '''


    


'''-------------------------- TEST ------------------------------'''

path_son="Musique/damso.mp3"
path_cover="Picture/CoverQALF.jpg"
GUI(path_son,path_cover)
