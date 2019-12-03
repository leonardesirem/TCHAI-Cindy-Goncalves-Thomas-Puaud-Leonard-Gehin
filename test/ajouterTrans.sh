#!/bin/bash/

curl --data "exp=c&dest=A&montant=20&submit=submit" http://127.0.0.1:5000/ajouterTransaction
curl --data "exp=C&dest=A&montant=10&submit=submit" http://127.0.0.1:5000/ajouterTransaction
curl --data "exp=C&dest=B&montant=50&submit=submit" http://127.0.0.1:5000/ajouterTransaction
curl --data "exp=B&dest=A&montant=25&submit=submit" http://127.0.0.1:5000/ajouterTransaction
