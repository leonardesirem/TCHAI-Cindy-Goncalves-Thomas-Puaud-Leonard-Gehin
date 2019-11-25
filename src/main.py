from flask import Flask, render_template, request
from datetime import datetime
import sqlite3 as sql
import os.path
app = Flask(__name__, template_folder = "template")

def init_db():
    nameFile = 'database.db'
    conn = sql.connect(nameFile)
    c = conn.cursor()
    
    if not os.path.isfile(nameFile):
        # Create table - Personne
        c.execute('''CREATE TABLE PERSONNE ([pers_id] INTEGER PRIMARY KEY, [nom] text, [solde] real)''')

        # Create table - Transaction
        c.execute('''CREATE TABLE TRANSACTION ([transaction_id] INTEGER PRIMARY KEY, [expediteur] INTEGER FOREIGN KEY, [destinataire] INTEGER FOREIGN KEY, [montant] real, [Date] date)''')

    conn.commit()

@app.route('/')
def home():
    return render_template('accueil.html')

@app.route('/ajouterTransaction')
def ajouterTransactionAccueil():
    return render_template('ajouterTransaction.html')

@app.route('/ajouterTransaction',methods = ['POST'])
def ajouterTransaction():
    try:
        exp = request.form['exp']
        dest = request.form['dest']
        montant = request.form['montant']
        date = str(datetime.now())

        with sql.connect("database.db") as con:
            cur = con.cursor()

            cur.execute("INSERT INTO transaction (exp,dest,montant,date) VALUES (?,?,?,?)",(exp,dest,montant,date) )
            #cur.execute("UPDATE personne SET personne.solde = personne.solde - montant WHERE personne=exp")
            #cur.execute("UPDATE personne SET personne.solde = personne.solde + montant WHERE personne=dest")

            con.commit()
            msg = "Transaction successfully added"
    except:
        con.rollback()
        msg = "Error in insert operation"

    finally:
        return render_template("result.html",msg = msg)
        con.close()

@app.route('/list', methods = ['GET'])
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from transaction order by date")

    rows = cur.fetchall();
    return render_template("list.html",rows = rows)
   
@app.route('/listParPers', methods = ['GET'])
def listParPers():   
    try:
        nom = request.form['nom']

        with sql.connect("database.db") as con:
            con.row_factory = sql.Row
            cur = con.cursor()

            cur.execute("select * from transaction where exp='nom' or dest='nom' order by date")
            rows = cur.fetchall();
    except:
        con.rollback()
        msg = "Echec de la récupération des données"

    finally:
        return render_template("listParPers.html",rows = rows)
        con.close()
		
@app.route('/soldeParPers', methods = ['GET'])
def soldParPers():   
    try:
        nom = request.form['nom']

        with sql.connect("database.db") as con:
            con.row_factory = sql.Row
            cur = con.cursor()

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













