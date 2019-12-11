from flask import Flask, render_template, request
from datetime import datetime
import sqlite3 as sql
import os.path
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
        
        p1=(exp,dest,montant,date)
        hashp1 = str(hash(p1))
        
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
    cur.execute("select * from tabletransaction")

    data = [[row[0],row[1],row[2],row[3],row[4],row[5]] for row in cur.fetchall()]
    
    somme = 0
    
    for row in data:
        p1=(row[1],row[2],row[3],row[4])
        hashp1 = str(hash(p1))
        
        msg = "Intégrité vérifiée"
        if hashp1 != row[5]:
            msg = "Intégrité corrompue"
        
        
    return render_template("integrite.html", msg=msg)

if __name__ == '__main__':
    init_db()
    app.run(debug = True, host='127.0.0.1')
