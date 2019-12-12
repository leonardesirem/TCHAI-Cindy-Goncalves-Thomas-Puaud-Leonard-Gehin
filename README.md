# Tchai (Transaction CHAIne)

Voici [le lien](https://kirgizov.link/teaching/esirem/advanced-information-systems-2019/TP-PROJET-TCHAI.pdf) vers la fiche du projet.

# Décision à travers le projet

Flask est un framework open-source de développement web en Python. Son but principal est d'être léger, afin de garder la souplesse de la programmation Python, associé à un système de templates.

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

# Version

## Tchai v1

Dans cette version, vous pouvez ajouter des transactions, les visualiser et voir le solde que possède un individu.

Vous pouvez exécuter le fichier `test/attaque1.py` pour démarrer une attaque sur la base de données et modifier le montant de la première transaction à 220. La base de données étant très simple, il suffit de modifier le montant d'une transaction pour faire une attaque avec succès.

## Tchai v2

Un hash est ajouté pour vérifier l'intégrité de nos données. Le serveur fonctionne de la même manière au niveau du client.

Pour verifier que la verification de l'integrite fonctionne bien dans le Tchai v2, vous pouvez vous placer dans le commit `768dd292413f25aeff94315e2806bfc178584552`. Veillez noter que dans ce commit, il se trouve un bug dont nous nous sommes rendu compte qu'a la fin du projet : Si vous redemarrer la session du serveur, la fonction de hashage donnera des donnees differente par rapport a la derniere session.

Pour l'attaque, vous pouvez lancer le script `test/attaqueExo8.py` pour supprimer la premiere requete de la base de donnees.

## Tchai v3

Les hashs sont maintenant calcules en utilisant le hash de la precedente transaction. Pour la premiere transaction, le hash precedent est initialise a `0`.

Les deux attaques precedente ne fonctionnent plus sur cette nouvelle base de donnees. Cependant, si la deuxieme attaque supprime la derniere transaction, la verification d'integrite des donnees ne s'en rendra pas compte.

De meme, si un attaquant pirate la base de donnees et ajoute des transactions a son benefice, il sera detecte par la verification d'integrite, sauf si le pirate ajoute son attaque malicieuse apres la derniere attaque.

Pour l'attaque, vous pouvez lancer le script `test/attaqueExo11.py` pour ajouter une requete apres la premiere presente dans la base. Cette requete redirigera l'argent de la premiere requete de la base de donnees vers le compte d'un certain "Leonard".

# Auteurs

- Cindy GONCALVES : goncalves.cindy@hotmail.fr (#peps0209)
- Thomas PUAUD : broz.jhimm@gmail.com (#frenchdogue)
- Leonard GEHIN : cuilliere169@gmail.com (#leonardesirem - #shaodwing)
