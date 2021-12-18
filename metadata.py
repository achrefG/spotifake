from tinytag import TinyTag



def Affiche_Metadonnee(filepath):
    '''
        Rôle:
            La fonction Affiche_Metadonee sert a renvoyer une liste contenant toutes les metadonées du fichier dont le chemin est donnée en entrée.
        Paramêtre : 
            filepath: Chemin du fichier audio( MP3/FLAC ) dont on veut recupérer les métadonnées.
        Sortie:
            Rien, Affichagde des metadonnées les plus importantes ( Artiste, Album , Titre , durée , ...)
    '''
    tag = TinyTag.get(filepath,image=True) # Utilisation de la methode TinyTag.get(Chemin_fichier,image=Boolean) pour recuperer dans une liste les metadonnées du fichier dont le chemin est donnée en paramêtre et sa coverture si elle existe au format binaire si le second parametre image=True.

    #Affichage des metadonnées qui nous interesses
    print("\nArtist: ", (tag.artist))
    print("Album: ", tag.album)
    print("Title: ", tag.title)
    print("Durée(secs): ",tag.duration)
    print("Musique N° ",tag.track)
    print("Compositeur:",tag.composer)
    print("Genre: "+str(tag.genre)+" \n")
    

def RecupMetadonneeListe(filepath):
    '''
        Rôle:
            La fonction RecupMetadonneeListe sert a renvoyer une liste contenant toutes les metadonées du fichier dont le chemin est donnée en entrée.
        Paramêtre : 
            filepath: Chemin du fichier audio( MP3/FLAC ) dont on veut recupérer les métadonnées.
        Sortie:
            tag: Liste contenant toutes métadonnées du fichier donnée en parametre.
    '''
    tag = TinyTag.get(filepath,image=True) # Utilisation de la methode TinyTag.get(Chemin_fichier,image=Boolean) pour recuperer dans une liste les metadonnées du fichier dont le chemin est donnée en paramêtre et sa coverture si elle existe au format binaire si le second parametre image=True.
        
    return tag




def metadata(filepath,Affichemeta):
    '''
        Rôle:
            La fonction metadata sert a renvoyer une liste contenant toutes les metadonées du fichier dont le chemin est donnée en entrée.
        Paramêtre : 
            filepath: Chemin du fichier audio( MP3/FLAC ) dont on veut recupérer les métadonnées.
            Affichemetadata: Boolean qui permet de savoir si on affiche les metadonnées en ligne de commande. (True: Appel de la methode Affiche_Metadonnee(filepath) qui affiche les metadonées || False : Appel de la methode RecupMetadonneeListe(filepath) qui renvoie une liste avec les metadonnées )
        Sortie:
            tag: Liste contenant toutes métadonnées du fichier donnée en parametre.
    '''

    if(Affichemeta==True): 
        print("Vous avez demandé l'affichage des métadonnées dans l'invite de commande, les voilà : ")
        Affiche_Metadonnee(filepath)

    elif(Affichemeta==False):
        #print("Vous avez demandé la recupération des métadonnées sous forme d'une liste. ")
        return RecupMetadonneeListe(filepath)
    else:
        print("Second parametre inconnu.")

'''--------------------------------------- TEST -------------------------------'''


#metadata("Musique/Vanille.mp3", True) # Affichage des metadonnées en ligne de commande.




#print(metadata("Musique/Vanille.mp3",False)) # Recuperation et Affichage d'une liste avec les metadonnées.

