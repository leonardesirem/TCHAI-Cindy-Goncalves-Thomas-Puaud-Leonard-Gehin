from flask import Flask, render_template, request
from datetime import datetime
import sqlite3 as sql
import os.path
import hashlib
app = Flask(__name__, template_folder = "template")
nameFileDatabase = './database.db'

def init_db():
    fichierExiste = not os.path.isfile(nameFileDatabase)
    conn = sql.connect(nameFileDatabase)
    c = conn.cursor()
    
    if fichierExiste:
        # Create table - Transaction
        c.execute('''CREATE TABLE TABLETRANSACTION ([transaction_id] INTEGER PRIMARY KEY, [expediteur] text, [destinataire] text, [montant] real, [Date] date, [hashp1] text)''')

    conn.commit()


@app.route('/')
def home():
    return render_template('accueil.html')

def recuperationDerniereLigneBdd(): 
    con = sql.connect(nameFileDatabase)
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from tabletransaction order by Date DESC limit 1")

    data = [[row[0],row[1],row[2],row[3],row[4],row[5]] for row in cur.fetchall()]  
    
    if len(data) > 0:
        # La base est deja remplie
        hashPrecedent = data[0][5]
    else:
        # La base est vide
        hashPrecedent = 0
    
    
    return str(hashPrecedent)
    
def calcHash(tupleToHash):
    tupleStr = '{}{}{}{}{}'.format(tupleToHash[0], tupleToHash[1], tupleToHash[2], tupleToHash[3], tupleToHash[4])
    return hashlib.md5(tupleStr.encode()).hexdigest()
    
@app.route('/ajouterTransaction')
def ajouterTransactionAccueil():
    return render_template('ajouterTransaction.html')


@app.route('/ajouterTransaction',methods = ['POST','GET'])
def ajouterTransaction():
    try:
        exp = request.form['exp'].lower()
        dest = request.form['dest'].lower()
        montant = float(request.form['montant'])
        date = str(datetime.now())
        
        hashPrecedent = recuperationDerniereLigneBdd();
        
        p1=(exp,dest,montant,date, hashPrecedent)
        hashp1 = calcHash(p1)
                
        if not montant:
            montant = 0

        with sql.connect(nameFileDatabase) as con:
            cur = con.cursor()

            cur.execute("INSERT INTO tabletransaction (expediteur,destinataire,montant,date,hashp1) VALUES (?,?,?,?,?)",(exp,dest,montant,date,hashp1))

            con.commit()
            msg = "La transaction a été ajoutée avec succès."
    except:
        con.rollback()
        msg = "Transaction échouée."

    finally:
        return render_template("result.html",msg = msg)
        con.close()


@app.route('/list', methods = ['GET'])
def list():
    con = sql.connect(nameFileDatabase)
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from tabletransaction order by date")

    rows = cur.fetchall();
    return render_template("list.html",rows = rows)
    
    
@app.route('/listParPersNom')
def listParPersNom():
    return render_template('listParPersNom.html')
   
    
@app.route('/listParPersNom', methods = ['POST','GET'])
def listParPers():   
    nom = request.form['nom'].lower()

    con = sql.connect(nameFileDatabase)
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from tabletransaction where expediteur=? or destinataire=? order by date", (nom,nom))

    rows = cur.fetchall();
    return render_template("listParPers.html",rows = rows)
   
   
@app.route('/soldeParPersNom')
def soldeParPersNom():
    return render_template('soldeParPersNom.html')

    
@app.route('/soldeParPersNom', methods = ['POST','GET'])
def soldParPers():   
    nom = request.form['nom'].lower()

    con = sql.connect(nameFileDatabase)
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from tabletransaction where expediteur=? or destinataire=? order by date", (nom,nom))

    data = [[row[0],row[1],row[2],row[3],row[4],row[5]] for row in cur.fetchall()]  
    print('data', data)
    
    somme = 0
    
    for row in data:
        # L'utilisateur est expediteur
        if row[1] == nom:
            somme -= row[3]
            
        # L'utilisateur est destinataire
        if row[2] == nom:
            somme += row[3]
    
    resultat = {
        'nom': nom,
        'montant': somme
    }
    
    return render_template("soldeParPers.html",resultat = resultat)
    
@app.route('/integrite', methods = ['POST','GET'])
def integrite():   

    con = sql.connect(nameFileDatabase)
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from tabletransaction order by date")

    data = [[row[0],row[1],row[2],row[3],row[4],row[5]] for row in cur.fetchall()]  
    
    if len(data) > 0:        
        msg = "Intégrité vérifiée"
        
        # L'ancien hash est initialise a 0 pour tester la premiere transaction
        ancienHash = 0
        for row in data:
            p1=(row[1],row[2],row[3],row[4], ancienHash)
            hashp1 = calcHash(p1)
            
            if hashp1 != row[5]:
                msg = "Intégrité corrompue"
            
            # Recupere hash actuel
            ancienHash = row[5]
    else:
        msg = "Il n'y a pas encore de données dans la base."
          
    return render_template("integrite.html", msg=msg)

if __name__ == '__main__':
    init_db()
    app.run(debug = True, host='127.0.0.1')

