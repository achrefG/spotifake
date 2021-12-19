import tkinter as tk
from tkinter import Button, filedialog
from tkinter.constants import COMMAND, NONE

from pygame import event

root = tk.Tk() # initialisation de la fenetre avec Tkinter
LST_Types = [ ( "Musique mp3" , ".mp3" ) , ( "Musique FLAC" , ".flac" ) ] # Liste comprenant les les extensions et type mimes accepté par notre filtres 
PL = [("PlayList xspf",".xspf")]

root.withdraw() # N'affiche que le derniere appel de fenetre


def getFile(): # MUSIQUE
    '''
        Rôle:
            La fonction getFile() sert à ouvrir une boite de dialgue qui sert a recupérer un fichier mp3 ou flac.
        Paramêtre : 
            Aucun
        Sortie:
            Affichagde de l'explorateur de recherche , avec les filtres mis donnée sous forme de liste en parametre.
            file_path: le chemin du fichier audio selectionné
    '''
    while True :
        file_path  = filedialog.askopenfilename(title = "Sélectionnez le son que vous voulez écouter ..." , filetypes = LST_Types)
        #print(file_path)
        if file_path.__len__()<3:
            print("ERREUR VOUS N'AVEZ RIEN SELECTIONNEE")
        else: 
            return file_path
def getFilePL(): # PlayList XSPF
    '''
        Rôle:
            La fonction getFilePL() sert à ouvrir une boite de dialgue qui sert a recupérer un fichier de PlayList XSPF.
        Paramêtre : 
            Aucun
        Sortie:
            Affichagde de l'explorateur de recherche , avec les filtres mis donnée sous forme de liste en parametre.
            file_path: le chemin du fichier audio selectionné
    '''
    while True :
        file_path  = filedialog.askopenfilename(title = "Sélectionnez la PlayList a ouvrire" , filetypes = PL)
        #print(file_path)
        if file_path.__len__()<3:
            print("ERREUR VOUS N'AVEZ RIEN SELECTIONNEE")
        else: 
            return file_path

def getDir():
    '''
        Rôle:
            La fonction getDir() sert à ouvrir une boite de dialgue qui sert a recupérer un fichier mp3 ou flac.
        Paramêtre : 
            Aucun
        Sortie:
            Affichagde de l'explorateur de recherche , avec les filtres mis donnée sous forme de liste en parametre.
            dir_path: le chemin du dossier selectionné
    '''
    while True :
        dir_path  = filedialog.askdirectory()
        #print(path)
        if dir_path.__len__()<3: 
                print("ERREUR VOUS N'AVEZ RIEN SELECTIONNEE")
        else:
            return dir_path


def getFiles(): # PLAYLIST
    '''
        Rôle:
            La fonction getFiles sert à ouvrir une boite de dialgue qui sert a recupérer un fichier mp3 ou flac.
        Paramêtre : 
            Aucun
        Sortie:
            Affichagde de l'explorateur de recherche , avec les filtres mis donnée sous forme de liste en parametre.
            file_paths: le chemin des fichiers audio selectionnée sous forme de liste
    '''
    while True :
        file_paths  = filedialog.askopenfilenames(title = "Sélectionnez la liste des fichier pour votre playliste" , filetypes = LST_Types)
        #print(file_paths)
        if str(file_paths).__len__()<3: 
            print("ERREUR VOUS N'AVEZ RIEN SELECTIONNEE")
        else:
            return file_paths


#------------------------------------------TETST ----------------------------------------

#getFile()
#getFiles()
#getDir()
