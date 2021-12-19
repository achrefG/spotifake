import os 

def parcour_directory(path):
    '''
        Rôle:
            La fonction parcour_directory sert a parcourir un dossier donnée en paramêtre et de retourner une liste contenant les chemins absolus des sous dossiers et fichiers qu'il contient.
        Paramêtre : 
            chemin_dossier: chemin du dossier qu'il faut parcourir.
        Sortie:
            liste: Contenant les sous dossiers et fichiers audio du dossier donné en entrée .
    '''
    liste= []
    for root, dirs, files in os.walk(path, topdown=False): # La methode os.walk(path,topdown) renvoi un triplet : os.walk[0]= chemin || os.walk[0]= nom_dossier || os.walk[2]= nom_fichier
        
        for name in files: # parcours de la liste files # contenant les noms des fichiers 
            liste.append(os.path.join(root, name)) # ajout des des chemins des fichiers, en fusionnat les chemins et les noms des fichiers
            #print(os.path.join(root, name))
        for name in dirs: # parcours de la liste dirs contenant les noms des dossiers
            liste.append(os.path.join(root, name))  # ajout des des chemins des dossiers, en fusionnat les chemins et les noms des dossiers
            #print(os.path.join(root, name))
    return(liste) #retourne une liste contenant les chemins des fichiers et sous dossiers du dossier donnée en parametre.




'''------------------------------------- TEST ---------------------------------------'''



#print(parcour_directory('C:\\Users\\charle\\Desktop\\W_PYTHON\\metadata_mp3-master\\Picture')) #TESTE PARCOURS LE DOSSIER PICTURE 

