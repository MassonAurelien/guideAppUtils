# coding=utf-8

import sqlite3
from pathlib import Path

def connection(chemin):
    if Path(chemin).exists() and Path(chemin).is_file() and chemin.find("NAMIP.db") !=-1:
        con = sqlite3.connect(chemin)
        cur = con.cursor()
        return con,cur
    else:
        print("Chemin d'accès éronné")
        exit()

def updateInsertTable(con,cur,requete,tableau):
    cur.executemany(requete,tableau)
    con.commit()