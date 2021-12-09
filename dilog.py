import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
LST_Types = [ ( "Musique mp3" , ".mp3" ) , ( "Musique FLAC" , ".flac" ) ]
root.withdraw()
def getFile():
    '''
    ouvre une boite de dialgue qui sert a recupérer un fichier mp3 ou flac
    return: le chemain du fichier
    '''
    file_path  = filedialog.askopenfilename(title = "Sélectionnez le son que vous voulez écouter ..." , filetypes = LST_Types)
    #print(file_path)
    return file_path
def getDir():
    '''
    ouvre une boite de dialgue qui sert a recupérer un repertoir
    return: le chemain du repertoir
    '''
    path  = filedialog.askdirectory()
    #print(path)
    return path
def getFiles():
    '''
    ouvre une boite de dialgue qui sert a recupérer une liste de fichier d'extention mp3 ou flac
    return: une liste de chemain de fichier
    '''
    file_paths  = filedialog.askopenfilenames(title = "Sélectionnez la liste des fichier pour votre playliste" , filetypes = LST_Types)
    #print(file_paths)
    return file_paths
#getFiles()
#getFiles()
#getDir()
