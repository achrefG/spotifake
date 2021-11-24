import sys 
from tinytag import TinyTag
import os

def metadata(filepath):
    tag = TinyTag.get(filepath)

    print("\nartist:", (tag.artist))
    print("album:", tag.album)
    print("title:", tag.title)
    print("duration(secs):",tag.duration)
    print("Musique N°",tag.track)
    print("Compositeur:",tag.composer)
    print("Genre:",tag.genre)
    #print()
    #print(tag) #print all metadata

def VerifExist(nom_fichier,liste):
    for i in liste:
        if (i == nom_fichier):
            return True
    return False

def parcour_dossier(path):

    dossier_path= path
    listefichier= []
    listedossier= []
    listefinale= []
    for chemin,dossiers,fichiers in os.walk(dossier_path): #fonction walk('path'), nous retournes un tableau qui en [0] contient les chemins , [1] contenant les sous dossiers , [2] les fichiers et sous fichiers
        for nom_file in fichiers:
            listefichier.append(nom_file)
        for nom_dir in dossiers:
            listedossier.append(nom_dir)

        for i in listedossier:
            if (VerifExist( i, listefinale)==0):
                listefinale.append(i)
        for j in listefichier:
            if (VerifExist( j, listefinale)==0):
                listefinale.append(j)
                            

    return listefinale


    

def main():
 
    if(len(sys.argv) == 1):
        print("Aucun paramemtre passe. Pour plus d'aide tapez -h ")
    elif(len(sys.argv)==2):

        if(sys.argv[1]==("-h")) :
            print("Les actions possibles sont : \n -d [chemin_dossier] pour parcourrir et afficher l'ensemble du dossier et ses sous dossiers \n -f [chemin_fichier_audio] pour obtenir les métadonnées du fichier '.mp3' ou '.flac' donnée en parametre \n -d [chemin_dossier] -o [nom_fichier_playlist_a_créer] pour crée une playlist grâce au fichier et sous dossier du dossier donnée en parametre \n " )
        elif(sys.argv[1]==("-f")):
            print("La commande n'est pas complete. Pour plus d'aide tapez -h")
        elif(sys.argv[1]==("-d")):
            print("La commande n'est pas complete. Pour plus d'aide tapez -h")
        else :
            print("La commande nexiste pas. Pour plus d'aide tapez -h")

    elif(len(sys.argv) == 3) :
        cheminfichier=sys.argv[2]
        if(sys.argv[1]==("-f") and sys.argv[2] != 0) :
            if (os.path.exists(cheminfichier) and os.path.isfile(cheminfichier)):
                metadata(cheminfichier)
            else:
                print("Le chemin de fichier audio donnée n'existe pas ou n'est pas celui d'un fichier")
        
        elif(sys.argv[1]==("-d") and sys.argv[2] != 0) : #Si l'argument n a pas de parametre cela indiquera Index 1 out of bounds
            if (os.path.exists(cheminfichier) and os.path.isdir(cheminfichier)):
                print("Ci-dessous vous avez tous les fichiers et dossiers presents dans le Dossier suiviant : "+ sys.argv[2])
                fichier_dossier= parcour_dossier(sys.argv[2])
                print(fichier_dossier)
            else:
                print("Le chemin du dossier donnée n'existe pas ou n'est pas celui d'un dossier")
        
        else:                                                        
            print("La commande est imcomplete ou nexiste pas. Pour plus d'aide tapez -h")      
                        
    elif(len(sys.argv) == 5) :
        if(sys.argv[1]==("-d") and sys.argv[2] != 0 and sys.argv[3]==("-o") and sys.argv[4] != 0 ) :
            print("LA CREATION DE LA PLAYLIST AU FORMAT XSPF ET UN AFFICHAGE DU FICHIER XSPF ")

    else:
        print("La commande est imcomplete ou nexiste pas. Pour plus d'aide tapez -h") 


main()

