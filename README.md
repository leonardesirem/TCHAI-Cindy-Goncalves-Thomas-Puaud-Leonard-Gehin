# Tchai (Transaction CHAIne)

Voici [le lien](https://kirgizov.link/teaching/esirem/advanced-information-systems-2019/TP-PROJET-TCHAI.pdf)
vers la fiche du projet.

# Decision a travers le projet

Nous avons choisie d'utiliser Flask avec python afin d'avoir un code simple sans trop de fioritures.

Pour la base de donnée, nous avons utilisé SQLite qui est léger et donc simple d'utilisation, comme son nom l'indique.

# Instruction pour l'utilisation du programme

Dépendance : ```Flask, Python (> 3.6), SQLite3```

Pour démarrer le serveur :
1. Placez vous dans le dossier racine du dossier
1. Lancez la commande ```python3 src/main.py```
1. Ensuite, connectez vous à l'adresse [127.0.0.1:5000](127.0.0.1:5000)

Exemple de requêtes HTTP :

```A faire```

# Tchai v1

Dans cette version, vous pouvez ajouter des transaction, les visualiser et voir le solde que possède un individus.

Vous pouvez exécuter le fichier ```test/attaque1.py``` pour démarrer une attaque sur la base de donnée et modifier le montant de la premiere transaction à 220. La base de donnée étant très simple, il suffit de modifier le montant d'une transaction pour faire une attaque avec succes.


# Auteurs

- Cindy GONCALVES : goncalves.cindy@hotmail.fr (#peps0209)
- Thomas PUAUD : broz.jhimm@gmail.com (#frenchdogue)
- Leonard GEHIN : cuilliere169@gmail.com (#leonardesirem)
