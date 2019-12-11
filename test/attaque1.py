import sqlite3 as sql
import numpy as np

# Doit etre lance depuit la racine du projet

def hack():
    # Chargement de la base
    nameFile = './database.db'

    con = sql.connect(nameFile)
    con.row_factory = sql.Row
    cur = con.cursor()

    cur.execute("select * from tabletransaction")

    data = [[row[0],row[1],row[2],row[3]] for row in cur.fetchall()]
    print(data)
    
    # Donnees qui seront modifie
    primaryKeyThatWillBeModified = 1
    newValue = 220  # approximatively pi
    
    # Injecte la nouvelle donnée
    cur.execute("UPDATE tabletransaction SET montant=? WHERE transaction_id=?",
                  (newValue, primaryKeyThatWillBeModified))
    
    con.commit()


if __name__ == '__main__':
    hack()
