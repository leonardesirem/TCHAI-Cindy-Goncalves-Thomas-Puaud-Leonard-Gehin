import sqlite3 as sql
import datetime
import hashlib

def calcHash(tupleToHash):
    tupleStr = '{}{}{}{}{}'.format(tupleToHash[0], tupleToHash[1], tupleToHash[2], tupleToHash[3], tupleToHash[4])
    return hashlib.md5(tupleStr.encode()).hexdigest()

# Doit etre lance depuit la racine du projet
def hack():
    # Chargement de la base
    nameFile = './database.db'

    con = sql.connect(nameFile)
    con.row_factory = sql.Row
    cur = con.cursor()

    cur.execute("select * from tabletransaction order by date")
    
    # Donnees qui seront modifie
    data = [[row[0],row[1],row[2],row[3],row[4],row[5]] for row in cur.fetchall()]
    
    # Calcul du hash voulu et de la date
    dataAvantCelleDeLattaquant = data[0]
    
    dateAvant = datetime.datetime.strptime(dataAvantCelleDeLattaquant[4], '%Y-%m-%d %H:%M:%S.%f')
    date = str(dateAvant + datetime.timedelta(seconds=1))
    transaction_id = len(data) + 1
    victime = dataAvantCelleDeLattaquant[2]
    montant = float(dataAvantCelleDeLattaquant[3])
    attaquant = 'cindy'
    hashDuPrecedent = dataAvantCelleDeLattaquant[5]
    
    p=(victime,attaquant,montant, date, hashDuPrecedent)
    hashTransaction = calcHash(p)
    
    # Injecte la nouvelle donnée
    cur.execute("INSERT INTO tabletransaction VALUES (?, ?,?,?,?,?)", (transaction_id, victime, attaquant, montant, date, hashTransaction))
    
    con.commit()

if __name__ == '__main__':
    hack()
