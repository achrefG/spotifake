import pygame
from PIL import Image

def liremusic_affichecover(path_son ,path_cover):

    cover= Image.open(path_cover) # ouverture de l'image donnee en parametre
    w,h=cover.size # stockage des dimensions de l'image 
    
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
    
    son = pygame.mixer.Sound(path_son) # creation de l'objet son grâce au path du fichier donnee en paramêtre
    son.play(0,0,0) #son.play(boucle=0,temps_max(en ms)=0 ,fondu au debut (en milliseconde)=0)

    son_cover = pygame.image.load(path_cover) # creation d'un nouvel objet image a partir d'un fichier donnee en paramêtre
    son_cover = pygame.transform.scale(son_cover , resolution_fenetre) # redimenssion de l'image a la taille de la fenêtre
    son_cover.convert() # conversion du format des pixels en un unique => facilites l'affichage
    #son_cover.set_colorkey((255,255,255)) # sert a rendre transparent(=> PNG ) les pixels de la couleur donnee en parametre 

    surface_fenetre.fill((0,0,0)) # fill : choix de la couleur pour le fond de la fenêtre
    surface_fenetre.blit(son_cover, [0,0]) # blit[0]: nom du fichier image et blit[1]: position du point en haut a gauche de l'image
    pygame.display.flip() # met a jour la fenêtre afficher
    
    lancer = True # boolean qui permet de garder la fenêtre ouverte tant quelle est vrai
    while lancer: # tant que lancer est vrai 
        for event in pygame.event.get(): # pour event variant en fonction de ce qu'il ce passe dans la fenêtre 
            if event.type == pygame.QUIT: # si l'evenement est : la fenetre est quitter 
                lancer = False # lancer devient faux et la fenêtre ne tourne plus 



    




path_son="Musique/Horizontal.mp3"
path_cover="Picture/CoverQALF.jpg"
liremusic_affichecover(path_son,path_cover)



""" RECUPERER EXTENSION D'UN FICHIER
    import os
 
    _, ext = os.path.splitext('/foo/bar/baz.txt')
    print ext # => .txt
"""