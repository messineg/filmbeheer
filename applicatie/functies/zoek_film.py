import sqlite3
from db.database import maak_connectie
from db.klassen import Film, Regisseur

def verkrijg_cursor():
	#Functie om niet telkens de code te moeten herhalen om de cursor op te halen
	dbconnectie= maak_connectie()
	cursor = dbconnectie.cursor()
	
	return dbconnectie, cursor

def zoek_film_titel():
	dbconnectie, cursor= verkrijg_cursor()

	gezochte_film = input("Geef de titel van een film in: ")
	
	cursor.execute('''SELECT Films.id, Films.titel, Films.release_jaar, Films.genre, 
		Regisseurs.naam, Regisseurs.geboorte_jaar 
		FROM Films
		JOIN Regisseurs ON Films.regisseur_id = Regisseurs.id 
		WHERE Films.titel LIKE ?''', (f"%{gezochte_film}%", ))
	
	for row in cursor:
		film = Film(row[0], row[1], row[2], row[3], row[4])
		regisseur = Regisseur(row[4], row[4], row[5])
		print("Filmgegevens:")
		film.beschrijf_film()
		print("Regisseurgegevens:")
		regisseur.beschrijf_regisseur()

def zoek_film_regisseur():
	dbconnectie, cursor= verkrijg_cursor()
	
	gezochte_regisseur = input("Geef de naam van een regisseur in: ")
	
	cursor.execute('''SELECT Films.id, Films.titel, Films.release_jaar, Films.genre, 
		Regisseurs.naam, Regisseurs.geboorte_jaar 
		FROM Films
		JOIN Regisseurs ON Films.regisseur_id = Regisseurs.id 
		WHERE Regisseurs.naam LIKE ?''', (f"%{gezochte_regisseur}%", ))
	
	for row in cursor:
		film = Film(row[0], row[1], row[2], row[3], row[4])
		regisseur = Regisseur(row[4], row[4], row[5])
		print("Filmgegevens:")
		film.beschrijf_film()
		print("Regisseurgegevens:")
		regisseur.beschrijf_regisseur()
