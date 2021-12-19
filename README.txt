Nom projet: Projet de PYTHON , Métadonnées de fichiers MP3/FLAC et playlist XSPF

Lien GITHUB : https://github.com/achrefG/spotifake/tree/master

Réaliser par : 
ABERKANE Mehdi GROUPE D 
GHEZIL Achref GROUPE B 
JAAFAR Amir GROUPE B
LINCENCE 3 INFORMATIQUE 

Résume:
   Notre logiciel en mode console et graphique permet l'extraction des métadonnée d'un fichier mp3/flac, de lancer un morceau ou encore de parcourir une arborescence de fichier afin d'extraire les fichiers mp3/flac avec vérification du type mime, et aussi voir le contenue d'une playlist xspf existante.

librairie utiliser :
    -tinytag
    -mimetypes
    -pygame
    -xspf_lib
    -tkinter


INFORMATION CÔTE CONSOLE (CLI): 
    -Pour lancer notre Commande Line Interface : 
        -Ouvrir un terminal deplacez vous dans le repertoire ou se trouve nos fichiers et tapez la commande : py CLI.py [suivi des arguments pour les commandes existantes] 
            -COMMANDES EXISTANTES:
                -d [chemin_dossier] pour parcourrir un dossier et ses sous dossiers et n'afficher que les fichiers audio (mp3/flac)   
                -f [chemin_fichier_audio] pour obtenir les métadonnées du fichier '.mp3' ou '.flac' donnée en parametre 
                -d [chemin_dossier] -o [nom_fichier_playlist_a_créer] pour crée une playlist grâce aux fichiers et sous dossier du dossier données en parametre 
                -l [chemin_fichier_audio] pour lire une musique 

Voilà vous pouvez profiter de notre CLI.



INFORMATION COTE GRAPHIQUE (GUI):
    -Pour lancer notre Commande Line Interface : 
        -Ouvrir un terminal deplacez vous dans le repertoire ou se trouve nos fichiers et tapez la commande : py GUI.py 
        -Notre Interface Graphique est normalement ouverte.
 
Voilà vous pouvez profiter de notre application SPOTIFAKE.