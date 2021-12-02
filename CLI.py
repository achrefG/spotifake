import sys 
from tinytag import TinyTag
import os

from metadata import metadata

from parcours_directory import parcour_directory

from Creatplaylist import VerifExtension, VerifMime, XspfPlaylist,RecupSong
    

def main():
 
    if(len(sys.argv) == 1):
        print("Aucun paramemtre passe. Pour plus d'aide tapez -h ou --help ")
    elif(len(sys.argv)==2):

        if(sys.argv[1]==("-h") or sys.argv[1]==("--help") ) :
            print("\nLes actions possibles sont : \n -d [chemin_dossier] pour parcourrir et afficher l'ensemble du dossier et ses sous dossiers \n -f [chemin_fichier_audio] pour obtenir les métadonnées du fichier '.mp3' ou '.flac' donnée en parametre \n -d [chemin_dossier] -o [nom_fichier_playlist_a_créer] pour crée une playlist grâce au fichier et sous dossier du dossier donnée en parametre \n " )
        elif(sys.argv[1]==("-f")):
            print("La commande n'est pas complete. Pour plus d'aide tapez -h")
        elif(sys.argv[1]==("-d")):
            print("La commande n'est pas complete. Pour plus d'aide tapez -h")
        else :
            print("La commande nexiste pas. Pour plus d'aide tapez -h")

    elif(len(sys.argv) == 3) :
        cheminfichier=sys.argv[2]
        if(sys.argv[1]==("-f") and sys.argv[2] != 0) :
            if (os.path.exists(cheminfichier) and os.path.isfile(cheminfichier) and VerifExtension(cheminfichier) and VerifMime ):
                metadata(cheminfichier)
            else:
                print("Le chemin de fichier audio donnée n'existe pas ou n'est pas celui d'un fichier MP3 ou FLAC")
        
        elif(sys.argv[1]==("-d") and sys.argv[2] != 0) : #Si l'argument n a pas de parametre cela indiquera Index 1 out of bounds
            if (os.path.exists(cheminfichier) and os.path.isdir(cheminfichier)):
                print("Ci-dessous vous avez tous les fichiers et dossiers presents dans le Dossier suiviant : "+ sys.argv[2])
                fichier_dossier= parcour_directory(sys.argv[2])
                liste_abspath_musique = RecupSong(fichier_dossier)
                for i in liste_abspath_musique:
                    print(i)
            else:
                print("Le chemin du dossier donnée n'existe pas ou n'est pas celui d'un dossier")
        
        else:                                                        
            print("La commande est imcomplete ou nexiste pas. Pour plus d'aide tapez -h")      
                        
    elif(len(sys.argv) == 5) :
        if(sys.argv[1]==("-d") and sys.argv[2] != 0 and sys.argv[3]==("-o") and sys.argv[4] != 0 ) :
            if (os.path.exists(sys.argv[2]) and os.path.isdir(sys.argv[2])): 
                TitrePlay=sys.argv[4]
                AuteurPlay= (input("Entrer le nom de l'auteur de la playlist : "))
                liste_abspath= parcour_directory(sys.argv[2])
                liste_abspath_musique = RecupSong(liste_abspath)
                XspfPlaylist(TitrePlay,AuteurPlay,liste_abspath_musique)
            else:
                print("Le chemin de dossier donné n'existe pas ou n'est pas celui d'un dossier. Pour plus d'aide tapez -h ")

    else:
        print("La commande est imcomplete ou nexiste pas. Pour plus d'aide tapez -h") 


main()