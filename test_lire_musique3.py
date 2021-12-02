import pygame

'''pygame.init(44100, 16, 2, 4096)
pygame.mixer.init(44100, -16, 2, 2048)'''
pygame.init() # initialisation de l'objet pygame
resolution_fenetre = (500,500) # paramêtrage de la taille de la fenêtre 
pygame.display.set_caption("Fenetre Python : JOUER UN SON")# Titre de la fenetre
surface_fenetre = pygame.display.set_mode(resolution_fenetre)
path=("Musique/Vanille.mp3")
son=pygame.mixer.music
son.load(path) # creation de l'objet son grâce au path du fichier donnee en paramêtre

son.play()

     

    #surface_fenetre.fill((0,0,0)) # fill : choix de la couleur pour le fond de la fenêtre
pygame.display.flip() # met a jour la fenêtre afficher

pause=False

lancer = True # boolean qui permet de garder la fenêtre ouverte tant quelle est vrai
while lancer: # tant que lancer est vrai 
    for event in pygame.event.get(): # pour event variant en fonction de ce qu'il ce passe dans la fenêtre 
        if event.type == pygame.QUIT: # si l'evenement est : la fenetre est quitter 
            lancer = False # lancer devient faux et la fenêtre ne tourne plus 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s and pause==False: #pause
                son.pause()
                pause=True
            if event.key == pygame.K_p : # replay
                son.rewind()

            if event.key == pygame.K_r and pause==True: # unpause
                son.unpause()

            if event.key == pygame.K_UP:
                son.set_volume(son.get_volume()+0.1)
            if event.key == pygame.K_DOWN:
                son.set_volume(son.get_volume()-0.1)



    



#path_son="C:/Users/kakif/Desktop/python/projet/Vanille.mp3"
#path_cover="Picture/CoverQALF.jpg"
#liremusic(path_son,path_cover)