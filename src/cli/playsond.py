import pygame
import io,sys
from PIL import Image
from pygame import draw
from metadata import metadata
from tinytag import TinyTag
import os

def playsond(path_son):
    '''
        Rôle:
            La fonction playsond sert a ecouter la musique d'un fichier audio donnée en parametre.
        Paramêtre : 
            path_son: Chemin du fichier audio( MP3/FLAC ) que l'on veut ecouter.
        Sortie:
            Affichagde de l'interface graphique pour ecouter le son avec sa cover et les plus importantes ( Artiste, Album , Titre , durée , ...)
    '''

    #--------------------------------------Recuperation de la cover de notre fichier audio si elle existe----------------------------------------
    
    path_cover="spotifake.png" # Path de la cover par defaut. Si le fichier audio n'a pas de cover on y met celui ci.

    meta = metadata(path_son,False) # Appel de la methode metadata avec le chemin du fichier du fichier audio et AfficheMeta=False car on ne veut pas afficher les metadonnées juste recupérer une liste.
    cover = meta.get_image() # Stockage de la cover sous forme de bytes si elle existe None sinon

    if(cover != None): # si le fichier audio a une cover 
        pi = Image.open(io.BytesIO(cover)) # ouverture de l'image avec PIL (avec conversion des bytes au format img) 
        
        print("\nLa cover du fichier audio que vous voulez jouer est "+ str(pi.format) + " retrouver la enregister dans Picture\cover."+str(pi.format)+"\n") # test pour connaitre le format de l'image decoder 
        
        cover = 'Picture\cover.'+str(pi.format) # enregistrement du nom de la cover decodée 'Picture\cover.'+ format de l'image decoder ( png ou jpeg )
        pi.save(cover) # enregistrement de l'image decodée 

    else: # si le fichier audio n'a  pas de cover 

        cover=path_cover  # attribution de la cover par defaut
    
    #--------------------------------------Creation et lancement de notre interface graphique ----------------------------------------

    pygame.init() # initialisation de l'objet pygame

    nomfichier=os.path.basename(path_son) # stockage du nom du fichier audio 

    pygame.display.set_caption(" VOUS ECOUTEZ LE FICHIER : "+str(nomfichier))# Titre de la fenetre
    
    
    # PRENDRE LA BONNE DIMMENSION // A MODIFIER QUAND INTERFACE GRAPHIQUE SERA EFFECTUEE

    resolution_fenetre= (500,600)
    surface_fenetre = pygame.display.set_mode(resolution_fenetre) # parametrage de la surface de la fenetre 
    

    son=pygame.mixer.music # sotckage de l'objet musiq de Pygame.mixer dans une variable
    son.load(path_son) # creation de l'objet son grâce au path du fichier donnee en paramêtre
    son.play(0,0,0) # lancement du fichier audio play(nombre de repetion, temps en seconde a partir du quel le son commence , fondu au lancement du fichier (ms) )
 
    son_cover = pygame.image.load(cover) # creation d'un nouvel objet image a partir d'un fichier donnee en paramêtre

    son_cover = pygame.transform.scale(son_cover , (400,400)) # redimenssion de l'image a la taille de la fenêtre
    
    son_cover.convert() # conversion du format des pixels en un unique => facilites l'affichage

    surface_fenetre.fill((0,0,0)) # fill : choix de la couleur pour le fond de la fenêtre
    surface_fenetre.blit(son_cover, [50,50]) # blit[0]: nom du fichier image et blit[1]: position du point en haut a gauche de l'image

    
    pause_img = pygame.image.load("Picture/pause.png") # creation d'un nouvel objet image a partir d'un fichier donnee en paramêtre
    unpause_img = pygame.image.load("Picture/unpause.png")
    up = pygame.image.load("Picture/up.png") 
    down = pygame.image.load("Picture/down.png")
    replay = pygame.image.load("Picture/replay.png")
    out = pygame.image.load("Picture/out.png") 



    surface_fenetre.blit(pause_img, [210,480])
    surface_fenetre.blit(out, [30,480])
    surface_fenetre.blit(replay, [120,480])
    surface_fenetre.blit(up, [390,480])
    surface_fenetre.blit(down, [300,480])
       
    black = pygame.Rect(0, 460, 500, 140)
    pause_button = pygame.Rect(210, 480, 80, 80) # appuis => met le son en pause ou relance si déja en pause
    up_button = pygame.Rect(390, 480, 80, 80) # appuis => volume up
    down_button = pygame.Rect(300, 480, 80, 80) # appuis => volume down
    replay_button = pygame.Rect(120, 480, 80, 80) # appuis => replay
    out_button = pygame.Rect(30, 480, 80, 80)

    #pygame.draw.rect(surface_fenetre,(255,0,255),pause_button)
    pygame.display.flip() # met a jour la fenêtre afficher
    #COMMANDES CLAVIERS EXISTANTES
    print("\n Commandes clavier de notre interface : \n - Taper sur H pour afficher les commandes existantes \n - Taper sur ESCAPE pour quitter l'interface graphique \n - Taper sur P pour: \n \t - mettre en pause la musique quand elle est lance \n \t - reprendre la musique quand elle est en pause \n - Taper sur R pour recommencer la musique \n - Taper sur FLECHE DU HAUT pour augmenter le son \n - Taper sur FLECHE DU BAS pour baisser le son \n  ")
    
    lancer = True # boolean qui permet de garder la fenêtre ouverte tant quelle est vrai
    click = False
    while lancer: # tant que lancer est vrai 
        mx, my = pygame.mouse.get_pos()
        if pause_button.collidepoint((mx, my)):# Si la touche entrer le button pause unpause et clicker
            if click:
                if son.get_busy()==True: # si le son tourne , get_busy() est une fonction qui retourne un boolean qui vaut TRUE si le son tourne et FALSE sinon
                    son.pause() # mise en pause
                    pygame.draw.rect(surface_fenetre,(0,0,0),black)
                    surface_fenetre.blit(replay, [120,480])
                    surface_fenetre.blit(up, [390,480])
                    surface_fenetre.blit(out, [30,480])
                    surface_fenetre.blit(down, [300,480])
                    surface_fenetre.blit(unpause_img, [210,480])
                    pygame.display.flip() 
                    print ("Vous avez mis pause")

                else:# si le son ne tourne pas , get_busy() est une fonction qui retourne un boolean qui vaut TRUE si le son tourne et FALSE sinon
                    son.unpause() # reprise 
                    print ("Vous avez relancé")
                    pygame.draw.rect(surface_fenetre,(0,0,0),black)
                    surface_fenetre.blit(replay, [120,480])
                    surface_fenetre.blit(out, [30,480])
                    surface_fenetre.blit(up, [390,480])
                    surface_fenetre.blit(down, [300,480])
                    surface_fenetre.blit(pause_img, [210,480])
                    pygame.display.flip()       
                click=False

        if replay_button.collidepoint((mx, my)):# Si la touche replay et clicker
            if click:
                #son.set_pos(0.0)
                son.rewind() # replay 
                print ("Vous avez recommencer la musique")
                click=False
        if son.get_pos()<0:
            son.stop() # Arret de la lecture de la musique
            son.unload() # dechargement du flux audio
            lancer = False # lancer devient faux et la fenêtre ne tourne plus => fermeture de la fenetre
        if up_button.collidepoint((mx, my)):# Si la touche "button pause unpause" est clicker
            if click:
                son.set_volume(son.get_volume()+0.1)# augmente le volume de 0.1
                print ("Vous avez augmenté le son de la musique. Son : "+str(son.get_volume())+"/ 1")
                click=False

        if down_button.collidepoint((mx, my)):# Si la touche volume down est clicker
            if click:
                son.set_volume(son.get_volume()-0.1)# baisse le volume de 0.1
                print ("Vous avez baissé le son de la musique. Son : "+str(son.get_volume())+"/ 1")
                click=False
        if out_button.collidepoint((mx, my)):# Si le button quité est et clicker
            if click:
                son.stop() # Arret de la lecture de la musique
                son.unload() # dechargement du flux audio
                lancer = False # lancer devient faux et la fenêtre ne tourne plus => fermeture de la fenetre
                click=False

        for event in pygame.event.get(): # pour event variant en fonction de ce qu'il ce passe dans la fenêtre 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.QUIT: # si l'evenement est : la fenetre est quitter 
                son.stop() # Arret de la lecture de la musique
                son.unload() # dechargement du flux audio
                lancer = False # lancer devient faux et la fenêtre ne tourne plus => fermeture de la fenetre
            
            elif event.type == pygame.KEYDOWN: # Parametrage des commandes par claviers
                Son_off =False # Boolean pour maitriser si le son est coupé ou non

                if event.key == pygame.K_h: # Si la touche entrer est H , affiche de l'aide
                    print("\n---------------------------------------------------------------------------------\n")
                    print("Commandes clavier de notre interface : \n - Taper sur ESCAPE pour quitter l'interface graphique \n - Taper sur P pour: \n \t - mettre en pause la musique quand elle est lance \n \t - reprendre la musique quand elle est en pause \n - Taper sur R pour recommencer la musique \n - Taper sur FLECHE DU HAUT pour augmenter le son \n - Taper sur FLECHE DU BAS pour baisser le son \n  ")
                    print("\n---------------------------------------------------------------------------------\n")
                
                elif event.key == pygame.K_p or pause_button.collidepoint((mx, my)):# Si la touche entrer est P
                    if son.get_busy()==True: # si le son tourne , get_busy() est une fonction qui retourne un boolean qui vaut TRUE si le son tourne et FALSE sinon 
                        son.pause() # mise en pause
                        pygame.draw.rect(surface_fenetre,(0,0,0),black)
                        surface_fenetre.blit(replay, [120,480])
                        surface_fenetre.blit(out, [30,480])
                        surface_fenetre.blit(up, [390,480])
                        surface_fenetre.blit(down, [300,480])
                        surface_fenetre.blit(unpause_img, [210,480])
                        pygame.display.flip() 
                        print ("Vous avez mis pause en tapant sur P")
                    else:# si le son ne tourne pas , get_busy() est une fonction qui retourne un boolean qui vaut TRUE si le son tourne et FALSE sinon
                        pygame.draw.rect(surface_fenetre,(0,0,0),black)
                        surface_fenetre.blit(replay, [120,480])
                        surface_fenetre.blit(out, [30,480])
                        surface_fenetre.blit(up, [390,480])
                        surface_fenetre.blit(down, [300,480])
                        surface_fenetre.blit(pause_img, [210,480])
                        pygame.display.flip() 
                        son.unpause() # reprise 
                        print ("Vous avez mis relancé en tapant sur P")
                        


                elif event.key == pygame.K_r : # Si la touche entrer est R
                    son.rewind() # replay
                    son.set_pos(0)
                    print ("Vous avez recommencer la musique en tapant sur R")
                    
                elif event.key == pygame.K_UP: # Si la touche entrer est FLECHE DU HAUT
                    son.set_volume(son.get_volume()+0.1)# augmente le volume de 0.1
                    print ("Vous avez augmenté le son de la musique en tapant sur FLECHE DU HAUT. Son : "+str(son.get_volume())+"/ 1")
                elif event.key == pygame.K_DOWN: # Si la touche entrer est FLECHE DU HAUT
                    son.set_volume(son.get_volume()-0.1)# baisse le volume de 0.1
                    print ("Vous avez baissé le son de la musique en tapant sur FLECHE DU BAS. Son : "+str(son.get_volume())+"/ 1")

                elif event.key == pygame.K_ESCAPE: # Si la touche entrer est ESCAPE
                    son.stop() # Arret de la lecture de la musique
                    son.unload() # dechargement du flux audio
                    lancer = False # lancer devient faux et la fenêtre ne tourne plus => fermeture de la fenetre
                
                else: # si une autre touche est entrée
                    print("- Taper sur H pour afficher les commandes existantes")
                    



'''-------------------------- TEST ------------------------------'''

#playsond('Musique\Mitsubishi.mp3')