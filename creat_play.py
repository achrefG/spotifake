import os
from os.path import *

import mimetypes


def VerifExtension(chemin):
    """
        Rôle:
            La fonction VerifExtension sert a verifier si l'extension du fichier dont le path est donnée en parametre est bien '.mp3' ou '.flac'.
        Paramêtre : 
            chemin: chemin pour acceder au fichier , dont il faut verifier l'extension
            
        Sortie:
            Boolean: 
                Vrai si le fichier est bien d'extension '.mp3' ou '.flac'. 
                Faux, si le chemin n'est pas celui d'un fichier, si le fichier n'existe pas ou si son extension n'est pas : '.mp3' ou '.flac'. 
    """
    name_fichier,extension=os.path.splitext(chemin)
    if (os.path.exists(chemin)):
        if(os.path.isfile(chemin)==0):
            print("Le path donnée n'est pas celui d'un fichier.")
            return False
        else:
            if(extension==".mp3" or extension==".flac"):
                print("Le fichier donné est bien d'extension mp3 ou flac.")
                return True
            else:
                print("Le fichier donnée n'est pas d'extension mp3 ou flac.")
                return False
    else:
        print("Le chemin n'existe pas.")
    


def VerifMime(chemin):
    if (os.path.exists(chemin)):
        if(os.path.isfile(chemin)==0):
            print("Le path donnée n'est pas celui d'un fichier.")
            return False
        else:
            type_mime_fichier=(mimetypes.guess_type(chemin))[0] #Stockage du type Mime du fichier dont on a donnée le chemin , renvoie un tuplet [type,encodage]
            if (type_mime_fichier=='audio/mpeg' or type_mime_fichier=='audio/x-flac'):
                print("Le fichier donné est bien de type mime mp3 ou flac.")
                return True
            else:
                print("Le fichier donné n'est pas de type mime mp3 ou flac.")
                return False
    else:
        print("Le chemin n'existe pas.")
    
def parcours_directory(path):

    listefichier= []

    for chemin,dossiers,fichiers in os.walk(path): #fonction walk('path'), nous retournes un tableau qui en [0] contient les chemins , [1] contenant les sous dossiers , [2] les fichiers et sous fichiers
        for nom_file in fichiers:
            
            listefichier.append(nom_file)

            
        #print( "FICHIER: " + str(listefichier ))
        return listefichier
        

def creat_play(chemin):
    liste=[]
    if (os.path.isfile(chemin)):
        if(VerifExtension(chemin)):
            if(VerifMime(chemin)):
                liste.append(chemin)

    elif(os.path.isdir(chemin)):
        
        liste_fichier=parcours_directory(chemin)
        for i in (liste_fichier):
            chemin_abs=os.path.abspath(i)
            liste.append(creat_play(chemin_abs))

    print(liste)



chemintest='C:/Users/charle/Desktop/W_PYTHON/Projet_Python/w_projet_python/metadata_mp3-1/Musique/'

#VerifMime(chemintest)
#print(VerifExtension('C:/Users/charle/Desktop/W_PYTHON/Projet_Python/w_projet_python/metadata_mp3-1/'))

creat_play(chemintest)