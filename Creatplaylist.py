from genericpath import exists
import os
from tinytag import TinyTag

import mimetypes

from parcours_directory import parcour_dossier

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
            #print("Le path donnée n'est pas celui d'un fichier.")
            return False
        else:
            if(extension==".mp3" or extension==".flac"):
                #print("Le fichier donné est bien d'extension mp3 ou flac.")
                return True
            else:
                #print("Le fichier donnée n'est pas d'extension mp3 ou flac.")
                return False
    else:
        print("Le chemin n'existe pas.")
    


def VerifMime(chemin):
    """
        Rôle:
            La fonction VerifExtension sert a verifier si le type mime du fichier dont le path est donnée en parametre est bien 'audio/mpeg' ou 'audio/x-flac'.
        Paramêtre : 
            chemin: chemin pour acceder au fichier , dont il faut verifier l'extension
            
        Sortie:
            Boolean: 
                Vrai si le fichier est bien de type mime 'audio/mpeg' ou 'audio/x-flac'.
                Faux, si le chemin n'est pas celui d'un fichier, si le fichier n'existe pas ou si son type mime n'est pas :'audio/mpeg' ou 'audio/x-flac'.
    """
    if (os.path.exists(chemin)):
        if(os.path.isfile(chemin)==0):
            #print("Le path donnée n'est pas celui d'un fichier.")
            return False
        else:
            type_mime_fichier=(mimetypes.guess_type(chemin))[0] #Stockage du type Mime du fichier dont on a donnée le chemin , renvoie un tuplet [type,encodage]
            if (type_mime_fichier=='audio/mpeg' or type_mime_fichier=='audio/x-flac'):
                #print("Le fichier donné est bien de type mime mp3 ou flac.")
                return True
            else:
                #print("Le fichier donné n'est pas de type mime mp3 ou flac.")
                return False
    else:
        print("Le chemin n'existe pas.")
    



def RecupSong(chemin_dossier,liste):
    '''
        Rôle:
            La fonction RecupSong sert a parcourir un dossier donnée en paramêtre et de stocker dans une liste que les fichiers audio plus précisement les fichiers MP3 ou FLAC.
        Paramêtre : 
            chemin_dossier: chemin du dossier qu'il faut parcourir
        Sortie:
            liste: Contenant les fichiers audio du dossier donné en entrée 
    '''
    liste_abs_path=parcour_dossier(chemin_dossier)
    
    for i in liste_abs_path:
        if (os.path.isfile(i)):
            if(VerifExtension(i)):
                if(VerifMime(i)):
                    liste.append(i)

    return(liste)



def XspfPlaylist(TitrePlay,AuteurPlay, liste_abspath_son):
    '''
        Rôle:
            La fonction XspfPlaylist sert a crée une playlist au format XSPF en parcourant une liste contenant les chemins absolu de fichiers audio
        Paramêtre : 
            TitrePlay: Titre de la paylist dans le fichier XSPF , mais également le nom du fichier XSPF
            AuteurPlay: Auteur de la paylist dans le fichier XSPF
            liste_abspath_son: liste contenant les chemins absolu qu'il faudra parcourir
        Sortie:
            Fichier XSPF , crée et rempli avec la playlist 
            + Affichage du contenu de ce fichier 
    '''
    TitreFichierXspf=TitrePlay+'.xspf'
    if (os.path.exists(TitreFichierXspf)):
        print("LE FICHIER XSPF EXISTE DEJA. REMISE A ZERO DU FICHIER "+ str(TitreFichierXspf) + " :" )
        file = open(TitreFichierXspf, "w") 
        TitreFichierXspf
        print (" SUCCES ")
        

        print("ECRITURE DE LA PLAYLIST "+ str(TitrePlay) +" DE "+ str (AuteurPlay) + " :"  )
        file.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n") 
        file.write("<playlist version='1' xmlns='http://xspf.org/ns/0/'>\n")
        file.write("	<title> "+TitrePlay+" </title>\n") 
        file.write("	<creator>"+AuteurPlay+"</creator>\n")
        file.write("	<info> .... </info>  \n")
        file.write("	<trackList>\n")

        for i in liste_abspath_son:
            tag = TinyTag.get(i)

            file.write("		<track>\n")
            file.write("			<creator> "+ str(tag.artist) +" </creator>\n")
            file.write("			<title> "+ str(tag.title) +" </title>\n")
            file.write("			<duration> "+ str(int(tag.duration))+" </duration>\n")
            file.write("			<album> "+ str(tag.album) +" </album>\n")
            file.write("			<location>file:"+i+"</location></track>\n")            

        file.write("	</trackList>\r\n" + "</playlist>")  

        print("ECRITURE TERMINER.")              
        
        file.close()
        
    else:
        print("LE FICHIER XSPF DONNE N'EXISTE PAS. CREATION DU FICHIER "+ str(TitreFichierXspf) + " :" )
        file = open(TitreFichierXspf, "x") 
        print("SUCCES")

        print("ECRITURE DE LA PLAYLIST "+ str(TitrePlay) +" DE "+ str (AuteurPlay) + " :" )
        file.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n") 
        file.write("<playlist version='1' xmlns='http://xspf.org/ns/0/'>\n")
        file.write("	<title> "+TitrePlay+" </title>\n") 
        file.write("	<creator>"+AuteurPlay+"</creator>\n")
        file.write("	<info> .... </info>  \n")
        file.write("	<trackList>\n")

        for i in liste_abspath_son:
            tag = TinyTag.get(i)

            file.write("		<track>\n")
            file.write("			<creator> "+str(tag.artist)+" </creator>\n")
            file.write("			<title> "+str(tag.title)+" </title>\n")
            file.write("			<duration> "+str(int(tag.duration))+" </duration>\n")
            file.write("			<album> "+ str(tag.album) +" </album>\n")
            file.write("			<location>file:"+i+"</location></track>\n")            

        file.write("	</trackList>\r\n" + "</playlist>")     

        print("ECRITURE TERMINER.")

        file.close()

    print("AFFICHAGE DE LA PLAYLIST " +str(TitrePlay)+ " :" )

    file=open(TitreFichierXspf, "r")
    
    file_read=file.read()

    print(file_read)


    file.close()



'''----------------------------------- TEST -----------------------------------'''



'''
liste=[]
listef=RecupSong('C:/Users/charle/Desktop/W_PYTHON/Projet_Python/w_projet_python/metadata_mp3-1/Musique/',liste)

XspfPlaylist("RAP_FR",'Mehdi',liste)'''

