import os 
from os.path import basename
from pathlib import Path


def VerifExist(nom_fichier,liste):
    '''
        Rôle:
            La fonction VerifExist sert à verifier si un fichier donné en parametre exist ou non dans la liste donné en parametre
        Paramêtre : 
            nom_fichier: Nom du fichier à verifier
            liste: liste a parcourir pour verifier si le fichier exist
        Sortie:
            liste: Contenant les sous dossiers et fichiers audio du dossier donné en entrée 
    '''
    for i in liste:
        if (i == nom_fichier):
            return True
    return False

    
def parcour_dossier(chemin_dossier):
    '''
        Rôle:
            La fonction parcour_dossier sert a parcourir un dossier donnée en paramêtre et de retourner une liste contenant les chemins absolu des sous dossiers et fichiers qu'il contient.
        Paramêtre : 
            chemin_dossier: chemin du dossier qu'il faut parcourir
        Sortie:
            liste: Contenant les sous dossiers et fichiers audio du dossier donné en entrée 
    '''
    listefichier= []
    listedossier= []
    listefinale= []
    save_dirname=os.path.dirname(chemin_dossier)+'/'
    if(os.path.isdir(chemin_dossier)):

        for chemin,dossiers,fichiers in os.walk(chemin_dossier): #fonction walk('path'), nous retournes un tableau qui en [0] contient les chemins , [1] contenant les sous dossiers , [2] les fichiers et sous fichiers
            for nom_file in fichiers:
                abs_path=save_dirname+nom_file
                listefichier.append(abs_path)
            for nom_dir in dossiers:
                abs_path=save_dirname+nom_dir
                listedossier.append(abs_path)

            for i in listedossier:
                if (VerifExist( i, listefinale)==0):
                    listefinale.append(i)
            for j in listefichier:
                if (VerifExist( j, listefinale)==0):
                    listefinale.append(j)
    else:
        listefinale.append(chemin_dossier)
        
                            

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


'''------------------------------------- TEST ---------------------------------------'''

'''
liste_abs_path=parcour_dossier('C:/Users/charle/Desktop/W_PYTHON/Projet_Python/w_projet_python/metadata_mp3-1/Musique')


for i in liste_abs_path:
    print(i)


'''