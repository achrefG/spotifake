import os
import mimetypes

from metadata import metadata


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
    if (os.path.exists(chemin)): # si le chemin existe
        if(os.path.isfile(chemin)==0): # si le chemin donnée est celui d'un fichier 
            #print("Le path donnée n'est pas celui d'un fichier.")
            return False
        else:
            type_mime_fichier=(mimetypes.guess_type(chemin))[0] #Stockage du type Mime du fichier dont on a donnée le chemin , ( mimetypes.guess_type(chemin) => renvoie un tuplet [type,encodage]
            if (type_mime_fichier=='audio/mpeg' or type_mime_fichier=='audio/x-flac'): # si le type mimes est celui d'un fichier mp3 ou FLAC
                #print("Le fichier donné est bien de type mime mp3 ou flac.") 
                return True
            else:
                #print("Le fichier donné n'est pas de type mime mp3 ou flac.")
                return False
    else:
        print("Le chemin n'existe pas.")
    




def RecupSong(liste):
    '''
        Rôle:
            La fonction RecupSong sert a parcourir un dossier donnée en paramêtre et de stocker dans une liste que les chemins des fichiers audio plus précisement les fichiers MP3 ou FLAC.
        Paramêtre : 
            liste: liste contenant les chemins à verifier des fichiers à verifiers
        Sortie:
            liste: Contenant les fichiers audio du dossier donné en entrée 
    '''
    #liste_abs_path=parcour_dossier(chemin_dossier)
    liste_song =[] # initialisation liste son 
    for i in liste: # parcours de la liste donnée en entrée
        if (os.path.isfile(i)): # si le chemine est celui d'un fichier
            if(VerifExtension(i)): #verification que son extension est bien ('.mp3' || '.flac')
                if(VerifMime(i)): #verification que son typemime :'audio/mpeg' ou 'audio/x-flac'
                    liste_song.append(i) # ajout du chemin dans la liste 

    return(liste_song)



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
    TitreFichierXspf=TitrePlay+'.xspf' # Nom du fichier XSPF qui contiendra la playlist 
    if (os.path.exists(TitreFichierXspf)): # si le fichier existe dejà 
        print("LE FICHIER XSPF EXISTE DEJA. REMISE A ZERO DU FICHIER "+ str(TitreFichierXspf) + " :" )
        file = open(TitreFichierXspf, "w") # Ouverture du fichier en ecriture pour réecrire par dessus l'ancienne playlist
        
        print (" SUCCES ")
        
        # ECRITURE DE LA PLAYLIST AU FORMAT XSPF
        print("ECRITURE DE LA PLAYLIST "+ str(TitrePlay) +" DE "+ str(AuteurPlay) + " :"  )
        file.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n") 
        file.write("<playlist version='1' xmlns='http://xspf.org/ns/0/'>\n")
        file.write("\t<title> "+TitrePlay+" </title>\n") 
        file.write("\t<creator>"+AuteurPlay+"</creator>\n")
        file.write("\t<trackList>\n")

        for i in liste_abspath_son: # Après avoir ecrit les information de bases , on ecrit les musiques de la playlist pour ça on parcours les fichier mp3/flac selectionnés
            tag = metadata(i,False) # pour chaque fichier fait appelle a la methode metadata pour recuperer les metadonnées sous forme de liste 
            
            file.write("\t\t<track>\n")
            file.write("\t\t\t<creator> "+str(tag.artist) +" </creator>\n")
            file.write("\t\t\t<title> "+ str(tag.title) +" </title>\n")
            file.write("\t\t\t<duration> "+ str(int(tag.duration))+" </duration>\n")
            file.write("\t\t\t<album> "+ str(tag.album) +" </album>\n")
            file.write("\t\t\t<location>file:"+i+"</location>\n")   
            file.write("\t\t</track>\n")            

        file.write("\t</trackList>\r\n" + "</playlist>")  

        print("ECRITURE TERMINER.")              
        
        file.close() # Fermerture du fichier ouvert 
        
    else:
        print("LE FICHIER XSPF DONNE N'EXISTE PAS. CREATION DU FICHIER "+ str(TitreFichierXspf) + " :" )
        file = open(TitreFichierXspf, "x") 
        print("SUCCES")

        # ECRITURE DE LA PLAYLIST AU FORMAT XSPF
        print("ECRITURE DE LA PLAYLIST "+ str(TitrePlay) +" DE "+ str (AuteurPlay) + " :" )
        file.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n") 
        file.write("<playlist version='1' xmlns='http://xspf.org/ns/0/'>\n")
        file.write("\t<title> "+TitrePlay+" </title>\n") 
        file.write("\t<creator>"+AuteurPlay+"</creator>\n")
        file.write("\t<trackList>\n")

        for i in liste_abspath_son: # Après avoir ecrit les information de bases , on ecrit les musiques de la playlist pour ça on parcours les fichier mp3/flac selectionnés
            tag = metadata(i,False) # pour chaque fichier fait appelle a la methode metadata pour recuperer les metadonnées sous forme de liste 
            
            file.write("\t\t<track>\n")
            file.write("\t\t\t<creator> "+str(tag.artist) +" </creator>\n")
            file.write("\t\t\t<title> "+ str(tag.title) +" </title>\n")
            file.write("\t\t\t<duration> "+ str(int(tag.duration))+" </duration>\n")
            file.write("\t\t\t<album> "+ str(tag.album) +" </album>\n")
            file.write("\t\t\t<location>file:"+i+"</location>\n")   
            file.write("\t\t</track>\n")            

        file.write("\t</trackList>\r\n" + "</playlist>")  

        print("ECRITURE TERMINER.")              
        
        file.close() # Fermerture du fichier ouvert 

    # AFFICHAGE DE LA PLAYLIST EN LIGNE DE COMMANDE : 

    print("AFFICHAGE DE LA PLAYLIST " +str(TitrePlay)+ " :" ) 

    file=open(TitreFichierXspf, "r") # OUVERTURE EN LECTURE 
    
    file_read=file.read() #LECTURE DU FICHIER

    print(file_read) # AFFFICHE CE QU'IL A LU


    file.close() # Fermerture du fichier ouvert 



'''----------------------------------- TEST -----------------------------------'''




#CREAT PLAYLIST AVEC LISTE
'''liste=['Musique/Vanille.mp3']
listef=RecupSong(liste)

XspfPlaylist("RAP_FR",'Mehdi',liste)'''

#print(VerifExtension('Musique/test.flac')) #VERIF EXTENSION

#VERIF MIME
'''print(VerifMime('Musique/Vanille.mp3'))
print(mimetypes.guess_type('Musique/Vanille.mp3'))'''
