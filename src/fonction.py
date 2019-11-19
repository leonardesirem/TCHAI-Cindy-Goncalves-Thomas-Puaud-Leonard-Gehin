import csv
import numpy as np


# Lit un fichier et retourne un tableau
def lireBaseDeDonnee(nomFichier):
	result = []
	with open(nomFichier, newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
		for row in spamreader:
			result.append(row)
	
	return result

# Ecrit un tableau dans un fichier csv
def ecrireBDD(nomFichier, donnee):
	with open(nomFichier, 'w', newline='') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=' ',
								quotechar='|', quoting=csv.QUOTE_MINIMAL)
		for row in donnee:
			spamwriter.writerow(row)

def transaction():
	return 0
	
def afficherListeTransaction():
	return 0
	
def afficherListeTransactionDe():
	return 0
	
def afficherSoldeCompte():
	return 0

def chargerDonnee():
	return 0




if __name__ == '__main__':
	testTab = [[1,2],[3,4]]
	ecrireBDD("test.csv", testTab)
	result = lireBaseDeDonnee("test.csv")
	
	print(result)
	
	#return 0
	



