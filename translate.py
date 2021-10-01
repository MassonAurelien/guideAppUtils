# coding=utf-8

#Partie traduction
import sqlite3
from google_translate_py import Translator
from database import connection,updateInsertTable

chemin = input("Chemin d'accès BD NAMIP: ")
#chemin = "C:/Users/aurel/github/guideApp/assets/database/NAMIP.db"
con,cur = connection(chemin)

def translate():
    list = [];
    for row in cur.execute('SELECT ID,DescFR,DescEN,DescNL FROM GENERAL;'):
        if row[2] is None or row[3] is None :
            enTranslate = Translator().translate(row[1],"fr","en")
            nlTranslate = Translator().translate(row[1],"fr","nl")
            list.append((enTranslate,nlTranslate,row[0]))
    return list

if con != None and cur != None:
    listeTranslate = translate()
    UpdateRequete = "UPDATE GENERAL SET DescEN = ? ,DescNL = ? WHERE ID = ?;"
    updateInsertTable(con,cur,UpdateRequete,listeTranslate)
    con.close()
    print("Traduction Effectuée")
