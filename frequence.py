#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 12:51:48 2022

@author: antonomaz
"""
import glob
import json
import re
import csv
from collections import OrderedDict





        
def nom_fichier(chemin):
    for mot in glob.glob(chemin): 
        noms_fichiers = re.split("/", chemin)
#        print("NOM FICHIER",noms_fichiers)
        
        nomsfich = re.split("\.",  noms_fichiers[3])
#        print(nomsfich)
    return nomsfich
        
def stocker( chemin, contenu):

    w =open(chemin, "w")
    w.write(json.dumps(contenu , indent = 2))
    w.close()
    print(chemin)
    
    return chemin
    



path_corpora = "./OUTPUT_BIO_SPACY/AUDOUX/audoux_PP_lg-spacy.bio"
#path_corpora = "../EN_DATA/corpora_EN_ALIGN_JSON2TXT/*/*/"
liste_recup_EN=[]
i=0

with open(path_corpora, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
#        print(', '.join(row))
#        liste_recup_EN.append(row)
#    nomfichier= nom_fichier(chemin)
#        for data in liste_recup_EN:
#            print(data)
        if row[1]== "B-LOC":
            i=i+1
            print(i)

#    dic_mots={}
#    i=0
    
#    for mot in liste_recup_EN:
#        
#        if mot not in dic_mots:
#            dic_mots[mot] = 1
#        else:
#            dic_mots[mot] += 1
#            #dic_langues[langue][mot] = dic_langues[langue][mot] + 1
#    
#    i += 1
##    print(dic_mots)
#    new_d = OrderedDict(sorted(dic_mots.items(), key=lambda t: t[0]))
#
##    print(new_d)
##    print(path_corpora)
#    freq=len(dic_mots.keys())
#    stocker("%s_frequence%s.json"%(chemin,freq), new_d)
    
#     

#    print("****************DIC MOTS KEYS",dic_mots.keys())
#    print(len(dic_mots.keys()))