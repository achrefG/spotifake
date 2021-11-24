import os 
from os.path import basename
from pathlib import Path



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



def parcour_directory_test(path,file_dir_filedir):

    dossier_path= path
    listefichier= []
    listedossier= []
    listefinale= []
    for chemin,dossiers,fichiers in os.walk(dossier_path): #fonction walk('path'), nous retournes un tableau qui en [0] contient les chemins , [1] contenant les sous dossiers , [2] les fichiers et sous fichiers
        if(file_dir_filedir==0):
            for nom_file in fichiers:
                listefichier.append(nom_file)
            for nom_dir in dossiers:
                listedossier.append(nom_dir)
            for i in listedossier:
                listefinale.append(i)
            for j in listefichier:
                listefinale.append(j)

            print( "DOSSIER:" + str(listedossier ))
            print( "FICHIER:" + str(listefichier))
            print( "LISTE: " + str(listefinale))
                            
            return listefinale
        elif(file_dir_filedir==1):
            for nom_dir in dossiers:
                listedossier.append(nom_dir)

            print( "DOSSIER: " + str(listedossier ))                
            return listedossier
                
        else:
            for nom_file in fichiers:
                listefichier.append(nom_file)

            print( "FICHIER: " + str(listefichier ))
                
            return listefichier




print (parcour_dossier('C:/Users/charle/Desktop/W_PYTHON/Projet_Python/w_projet_python/metadata_mp3-1/Musique'))







