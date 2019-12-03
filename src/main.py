from flask import Flask, render_template, request
from datetime import datetime
import sqlite3 as sql
import os.path
app = Flask(__name__, template_folder = "template")

def init_db():
    nameFile = 'database.db'
    fichierExiste = not os.path.isfile(nameFile)
    conn = sql.connect(nameFile)
    c = conn.cursor()
    
    if fichierExiste:
        # Create table - Transaction
        c.execute('''CREATE TABLE TABLETRANSACTION ([transaction_id] INTEGER PRIMARY KEY, [expediteur] text, [destinataire] text, [montant] real, [Date] date)''')

    conn.commit()

@app.route('/')
def home():
    return render_template('accueil.html')

@app.route('/ajouterTransaction')
def ajouterTransactionAccueil():
    return render_template('ajouterTransaction.html')

#tester si on peut enlever le GET ci-dessous
@app.route('/ajouterTransaction',methods = ['POST','GET'])
def ajouterTransaction():
    try:
        exp = request.form['exp'].lower()
        dest = request.form['dest'].lower()
        montant = request.form['montant']
        date = str(datetime.now())
        
        if not montant:
            montant = 0

        with sql.connect("database.db") as con:
            cur = con.cursor()

            cur.execute("INSERT INTO tabletransaction (expediteur,destinataire,montant,date) VALUES (?,?,?,?)",(exp,dest,montant,date))

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
    con = sql.connect("database.db")
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

    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from tabletransaction where expediteur=? or destinataire=? order by date", (nom,nom))

    rows = cur.fetchall();
    return render_template("listParPers.html",rows = rows)
   
# @app.route('/listParPers', methods = ['GET'])
# def listParPers():   
    # try:
        # nom = request.form['nom'].lower()

        # with sql.connect("database.db") as con:
            # con.row_factory = sql.Row
            # cur = con.cursor()

            # cur.execute("select * from tabletransaction where expediteur=? or destinataire=? order by date", (nom,))
            # rows = cur.fetchall();
    # except:
        # con.rollback()
        # msg = "Echec de la récupération des données"

    # finally:
        # return render_template("listParPers.html",rows = rows)
        # con.close()
		
        
#A modifier totalement car on n'a plus de table personne        
@app.route('/soldeParPers', methods = ['GET'])
def soldParPers():   
    try:
        nom = request.form['nom']

        with sql.connect("database.db") as con:
            con.row_factory = sql.Row
            cur = con.cursor()
            #Requete à modifier en prenant en compte la suppression de la table personne
            cur.execute("select solde from personne where personne.nom='nom'")
            rows = cur.fetchall();
            msg = "Transaction successfully added"
    except:
        con.rollback()
        msg = "Echec de la récupération des données"

    finally:
        return render_template("soldeParPers.html",rows = rows)
        con.close()

if __name__ == '__main__':
    init_db()
    app.run(debug = True)
