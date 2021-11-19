import pygame
import os

def liremusic(path_son ,path_cover):
    
    pygame.init() # initialisation de l'objet pygame
    resolution_fenetre = (500,500) # paramêtrage de la taille de la fenêtre 
    
    pygame.display.set_caption("Fenetre Python : JOUER UN SON")# Titre de la fenetre
    surface_fenetre = pygame.display.set_mode(resolution_fenetre)
    
    son = pygame.mixer.Sound(path_son) # creation de l'objet son grâce au path du fichier donnee en paramêtre
    son.play(0,0,0) #son.play(boucle=0,temps_max(en ms)=0 ,fondu au debut (en milliseconde)=0)


    surface_fenetre.fill((0,0,0)) # fill : choix de la couleur pour le fond de la fenêtre
    pygame.display.flip() # met a jour la fenêtre afficher
    
    lancer = True # boolean qui permet de garder la fenêtre ouverte tant quelle est vrai
    while lancer: # tant que lancer est vrai 
        for event in pygame.event.get(): # pour event variant en fonction de ce qu'il ce passe dans la fenêtre 
            if event.type == pygame.QUIT: # si l'evenement est : la fenetre est quitter 
                lancer = False # lancer devient faux et la fenêtre ne tourne plus 



    




path_son="Musique/Horizontal.mp3"
path_cover="Picture/CoverQALF.jpg"
liremusic(path_son,path_cover)



""" RECUPERER EXTENSION D'UN FICHIER
    import os
 
    _, ext = os.path.splitext('/foo/bar/baz.txt')
    print ext # => .txt
"""