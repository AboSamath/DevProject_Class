# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 10:11:52 2023

@author: DELL
"""

# YATTE Abdou Samath | Master 1 Intellligence Artificielle Session Janv 23

# Exercice 44 

#Déclaration de la fonction

def read_file(path = r"C:\Users\DELL\Desktop\Abo\Perso\Master 1 IA DIT\Python\YATTE_Abdou_Samath_DS\dataset.txt"):
    
    # Noter que le chemin assigner à la variable devrait être changer en fonction de l'emplacement du fichier 
    
    # Ouverture du fichier
    f = open(path)
    
    #Déclaration de deux listes vides dans lesquelles seront stockées les résultats
    Xvec = []
    Yvec = []
    
    #création d'une liste vide pour stockage des données
    List_donnees = [] 
    
    #Lecture et affichage des données contenus dans le fichier
    for x in f:
        #Recupération des coordonnées abscisses et ordonnées dans une liste
        L = x.split(";")
        print(x)
        
        # Parcourir chaque sous-liste et diviser chaque élément en utilisant "," comme séparateur
        for m in L:
            elements = m.split(",")
            List_donnees.append(elements)
        
        #Conversion de la nouvelle liste constitué de tuples en entier
        List_entier = []
        for n in List_donnees:
            if n[0] != "Null" and n[1] != "Null":
                List_entier.append((int(n[0]), int(n[1])))
            elif n[0] != "Null":
                List_entier.append((int(n[0]), None))
            elif n[1] != "Null":
                List_entier.append((None, int(n[1])))
            else:
                List_entier.append((None, None))
            
        #Classement des éléments en abscisse et ordonnées
        for i in List_entier:
            if i[0] is not None:
                Xvec.append(i[0])
            if i[1] is not None:
                Yvec.append(i[1])
        
            
        print("\n")
      
    return print("Xvec = ", Xvec,"\nYvec = ", Yvec)

read_file()