# Tchai (Transaction CHAIne)

Voici [le lien](https://kirgizov.link/teaching/esirem/advanced-information-systems-2019/TP-PROJET-TCHAI.pdf) vers la fiche du projet.

# Decision a travers le projet

Nous avons choisi d'utiliser Flask avec Python afin d'avoir un code simple sans trop de fioritures.

Pour la base de données, nous avons utilisé SQLite qui est léger et donc simple d'utilisation, comme son nom l'indique. Pour visualiser nos données, nous avons utiliser le logiciel libre qui s'appelle DB Browser for SQLite.

# Instruction pour l'utilisation du programme

Dépendance : ```Flask, Python (> 3.6), SQLite3```

Pour démarrer le serveur :
1. Placez vous dans le dossier racine du dossier
1. Lancez la commande ```python3 src/main.py``` (pour Windows : remplacez / par \)
1. Ensuite, connectez vous à l'adresse [127.0.0.1:5000](127.0.0.1:5000)

Exemples de requêtes HTTP :

- Ajouter une transaction

```curl --data "exp=A&dest=B&montant=30" http://127.0.0.1:5000/ajouterTransaction```


- Consulter la liste de toutes les transactions dans l'ordre chronologique

```curl http://127.0.0.1:5000/list```


- Consulter la liste des transactions concernant une personne en particulier dans l'ordre chronologique

```curl --data "nom=cindy" http://127.0.0.1:5000/listParPersNom```


- Consulter le solde d'une personne en particulier

```curl --data "nom=cindy" http://127.0.0.1:5000/soldeParPersNom```


- Vérifier l'intégrité des données

```curl http://127.0.0.1:5000/integrite```

# Tchai v1

Dans cette version, vous pouvez ajouter des transactions, les visualiser et voir le solde que possède un individu.

Vous pouvez exécuter le fichier ```test/attaque1.py``` pour démarrer une attaque sur la base de données et modifier le montant de la première transaction à 220. La base de données étant très simple, il suffit de modifier le montant d'une transaction pour faire une attaque avec succès.

# Tchai v2

Un hash est ajouté pour vérifier l'intégrité de nos données. Le serveur fonctionne de la même manière au niveau du client.

Pour verifier que la verification de l'integrite fonctionne bien, vous pouvez vous placer dans le commit ```768dd292413f25aeff94315e2806bfc178584552```

# Auteurs

- Cindy GONCALVES : goncalves.cindy@hotmail.fr (#peps0209)
- Thomas PUAUD : broz.jhimm@gmail.com (#frenchdogue)
- Leonard GEHIN : cuilliere169@gmail.com (#leonardesirem - #shaodwing)

