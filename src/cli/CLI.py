import sys 
from tinytag import TinyTag
import os

from metadata import metadata

from parcours_directory import parcour_directory

from Creatplaylist import VerifExtension, VerifMime, XspfPlaylist,RecupSong

from playsond import playsond
    

def main():
    """
        Rôle: Grâce au CLI il est possible d'effectuer plusieurs actions possibles:
            -Afficher les metadonnées , d'un fichier audio donnée en argument (py CLI.py -f [chemin_fichier_audio])
            -Afficher les fichiers audio ( mp3 / flac ) d'un dossier en explorant lui meme et ses sous dossiers , dont le chemin du dossier est donnée en argument (py CLI.py -d [chemin_dossier])
            -Lire une musique , dont le chemin est donnée ene argument (py CLI.py -l [chemin_fichier_audio])
            -Créer une playlist dont le nom est donnée en parametre, grâce aux fichiers audios de dossier donné en argument (py CLI.py -d [chemin_dossier] -o [nom_fichier_playlist_a_créer] )
        Paramêtre : 
            Aucun, ils sont données en argument 
        Sortie:
            Affichage en console.
    """

    print ("--------------------------------------------------------------------------------------------------------------------------")
 
    if(len(sys.argv) == 1): #si le nombre d'arguments donné est de 1 c'est à dire qu'aucun argument est entrée ( le nom du fichier à la place argv[0] )
        print("Aucun paramemtre passe. Pour plus d'aide tapez -h ou --help ") # Affichage d'un message pour plus d'aide 
    
    elif(len(sys.argv)==2): #si la longueur des arguments donné est de 2 

        if(sys.argv[1]==("-h") or sys.argv[1]==("--help") ) : #Si l'argument 1 est -h ou --help 
            print("\nLes actions possibles sont : \n -d [chemin_dossier] pour parcourrir un dossier et ses sous dossiers et n'afficher que les fichiers audio (mp3/flac)   \n -f [chemin_fichier_audio] pour obtenir les métadonnées du fichier '.mp3' ou '.flac' donnée en parametre \n -d [chemin_dossier] -o [nom_fichier_playlist_a_créer] pour crée une playlist grâce au fichier et sous dossier du dossier donnée en parametre \n -l [chemin_fichier_audio] pour lire une musique " )
        
        elif(sys.argv[1]==("-f")):#Si l'argument est -f 
            print("La commande n'est pas complete. Pour plus d'aide tapez -h") # Affichage d'un message pour plus d'aide 
        
        elif(sys.argv[1]==("-d")): #Si l'argument est -d 
            print("La commande n'est pas complete. Pour plus d'aide tapez -h") # Affichage d'un message pour plus d'aide 
        
        else : #Si l'argument est autre que ceux definit ci-dessus 
            print("La commande nexiste pas. Pour plus d'aide tapez -h") # Affichage d'un message pour plus d'aide 

    elif(len(sys.argv) == 3) : #si la longueur des arguments donné est de 3 
        chemin=sys.argv[2] #stockage du chemin dans une variable 
        if(sys.argv[1]==("-f") and sys.argv[2] != 0) : # si le premier argument est '-f' et que le second n'est pas null
            
            if (os.path.exists(chemin) and os.path.isfile(chemin) and VerifExtension(chemin) and VerifMime(chemin) ):# si le chemin existe , si c'est celui d'un fichier , si l'extension et le types mimes est le bon
                metadata(chemin,True) # appel de la methode metadata(chemin_du_fichier ,Boolean_Affiche_en_console )
            else:
                print("Le chemin de fichier audio donnée n'existe pas ou n'est pas celui d'un fichier MP3 ou FLAC")
        
        elif(sys.argv[1]==("-d") and sys.argv[2] != 0) : #  si le premier argument est '-d' et que le second n'est pas nul 
            if (os.path.exists(chemin) and os.path.isdir(chemin)): # si le chemin existe et si c'est celui d'un repertoire
                
                print("Ci-dessous vous avez les fichiers audios du dossier et des sous dossiers de "+ sys.argv[2])
                fichier_dossier= parcour_directory(sys.argv[2]) # appel de la fonction parcour_directory qui recupere tous les chemins des dossiers et fichiers du dossier donné en argument.
                liste_abspath_musique = RecupSong(fichier_dossier) # appel de la focntion RecupSong , qui ne garde que les chemin des fichiers audios ( mp3/ flac ) avec verification de l'extension et du type mimes
                
                for i in liste_abspath_musique: #parcours de la liste avec les chemins des fichiers audios 
                    print(i) #affichages des chemins 
            
            else:#si le chemin n'existe pas 
                print("Le chemin du dossier donnée n'existe pas ou n'est pas celui d'un dossier")

        elif(sys.argv[1]==("-l") and sys.argv[2] != 0) :# si le premier argument est '-l' et que le second n'est pas nul 
            
            if (os.path.exists(chemin) and os.path.isfile(chemin) and VerifExtension(chemin) and VerifMime(chemin) ):# si le chemin existe , si c'est celui d'un fichier , si l'extension et le types mimes est le bon
                path_son=chemin # stockage du chemin dans une variable de passage 
                playsond(path_son) # appel de la methode playsond() pour lire le son 
            
            else:# sinon
                print("Le chemin de fichier audio donnée n'existe pas ou n'est pas celui d'un fichier MP3 ou FLAC")
        
        else: # sinon                                                       
            print("La commande est imcomplete ou nexiste pas. Pour plus d'aide tapez -h")      
                        
    elif(len(sys.argv) == 5) : #si la longueur des arguments donné est de 5 
        
        if(sys.argv[1]==("-d") and sys.argv[2] != 0 and sys.argv[3]==("-o") and sys.argv[4] != 0 ) : # si le premier argument est '-d' et que le second n'est pas null , que le troisieme est '-o' et que le quatrieme n'est pas null
            if (os.path.exists(sys.argv[2]) and os.path.isdir(sys.argv[2])): # si l'argument 2 est celui d'un chemin existant et si c'est celui d'un repertoire
                
                TitrePlay=sys.argv[4] # Stockage de l'argument 4 qui est le nom de la playlist et du fichier XSPF
                AuteurPlay= (input("Entrer le nom de l'auteur de la playlist : ")) # formulaire pour demander le nom de l'auteur de la playlist 
                liste_abspath= parcour_directory(sys.argv[2]) # appel de la fonction parcour_directory qui recupere tous les chemins des dossiers et fichiers du dossier donné en argument.
                liste_abspath_musique = RecupSong(liste_abspath) # appel de la focntion RecupSong , qui ne garde que les chemin des fichiers audios ( mp3/ flac ) avec verification de l'extension et du type mimes
                XspfPlaylist(TitrePlay,AuteurPlay,liste_abspath_musique) # appel de la methode XspfPlaylist qui va créer une playlist au format XSPF avec la liste de chemin de fichier mp3 donnée en parametre
            
            else:# sinon
                print("Le chemin de dossier donné n'existe pas ou n'est pas celui d'un dossier. Pour plus d'aide tapez -h ")

    else:#si la longueur des arguments donné est differente de celle definit ci-dessus
        print("La commande est imcomplete ou nexiste pas. Pour plus d'aide tapez -h") 


main()