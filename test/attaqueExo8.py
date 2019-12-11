import sqlite3 as sql

# Doit etre lance depuit la racine du projet
def hack():
    # Chargement de la base
    nameFile = './database.db'

    con = sql.connect(nameFile)
    con.row_factory = sql.Row
    cur = con.cursor()

    cur.execute("select * from tabletransaction")
    
    # Donnees qui seront modifie
    primaryKey = [row[0] for row in cur.fetchall()]
    primaryKeyThatWillBeModified = primaryKey[0]
    
    # Injecte la nouvelle donnée
    cur.execute("DELETE FROM tabletransaction WHERE transaction_id=?", (primaryKeyThatWillBeModified,))
    
    con.commit()


if __name__ == '__main__':
    hack()
