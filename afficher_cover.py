import pygame
from PIL import Image 


"""
    OPTION pygame.display.setmode(......)
    pygame.FULLSCREEN : fenetre en pleine ecran 
    pygame.RESIZABLE : fenetre redimanssionable
    pygame.NOFRAME : fenetre sans control ( pas de bandeau pour le nom ou pour la fermer )
"""


def afficher_cover(path_cover):

    cover= Image.open(path_cover) # ouverture de l'image donnee en parametre
    w,h=cover.size # stockage des dimensions de l'image 
    
    pygame.init() # initialisation de l'objet pygame
    pygame.display.set_caption(" AFFICHE COVER ")# Titre de la fenetre
    

    # PRENDRE LA BONNE DIMMENSION // A MODIFIER QUAND INTERFACE GRAPHIQUE SERA EFFECTUEE
    if ((w==h) and (w>800)):
        resolution_fenetre = (500,500) # taille de la fenêtre 
    elif((w!=h and (w>1000 or h>800))):
        resolution_fenetre = (w/2,h/2) # taille de la fenêtre 
    else:
        resolution_fenetre= (w,h)

    
    surface_fenetre = pygame.display.set_mode(resolution_fenetre) # parametrage de la surface de la fenetre 

    son_cover = pygame.image.load(path_cover) # creation d'un nouvel objet image a partir d'un fichier donnee en paramêtre
    son_cover = pygame.transform.scale(son_cover , resolution_fenetre) # redimenssion de l'image a la taille de la fenêtre
    son_cover.convert() # conversion du format des pixels en un unique => facilites l'affichage
    #son_cover.set_colorkey((255,255,255)) 

    surface_fenetre.fill((255,255,255)) # fill : choix de la couleur pour le fond de la fenêtre
    surface_fenetre.blit(son_cover, [0,0]) # blit[0]: nom du fichier image et blit[1]: position du point en haut a gauche de l'image
    pygame.display.flip() # met a jour la fenêtre afficher

    lancer = True # boolean qui permet de garder la fenêtre ouverte tant quelle est vrai
    while lancer: # tant que lancer est vrai 
        for event in pygame.event.get(): # pour event variant en fonction de ce qu'il ce passe dans la fenêtre 
            if event.type == pygame.QUIT: # si l'evenement est : la fenetre est quitter 
                lancer = False # lancer devient faux et la fenêtre ne tourne plus 


    




afficher_cover("Picture/CoverQALF.jpg")
#afficher_cover("Picture/QALFimage.jpg")
#afficher_cover("Picture/don_dada _mixtape_cover.jpg")
#afficher_cover("Picture/lama.png")























"""import pygame
from pygame.constants import K_SPACE 

pygame.init()
pygame.display.set_caption("Ma premiere fenetre ")

fenetre = pygame.display.set_mode((640,480))
info =pygame.display.Info() # recup des infos de la fenetre 
print (pygame.display.Info().current_w)


fenetre.fill((255,255,255))




pygame.draw.line(fenetre, (0,0,0) , [10,10] , [50, 50])

rectangle = pygame.Rect(100,100, 150, 65)
pygame.draw.rect(fenetre, (0,0,0) , rectangle , 1) # rectangle plein  ||pygame.draw.rect(fenetre ou sera le rectangle , couleur , forme a afficher  , largeur bordure )

pygame.draw.circle( fenetre , (0,0,0) , [400 , 300 ],  20 , 1)


coords = [(500,400) , (510,400) , (510,410) ,(500,410)]
pygame.draw.polygon( fenetre , (0,0,0) , coords , 1 )

pygame.display.flip()

lancer = True
while lancer:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            lancer = False
        
            




"""