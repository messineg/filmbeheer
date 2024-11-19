import sqlite3
from db.database import verkrijg_cursor
from db.klassen import Film, Regisseur
from functies.toon_gegevens import toon_films_alle, toon_regisseurs_alle

def voeg_film_toe():
	dbconnectie, cursor = verkrijg_cursor()

	film_titel = input("Geef de titel van een film in: ")
	film_release = int(input("Geef releasejaar: "))
	film_genre = input("Geef het genre in: ")
	film_regisseur = input("Geef regisseur: ")

	#Controle om te checken of de regisseur al bestaat
	query_regisseur = 'SELECT * FROM Regisseurs WHERE naam=?'
	cursor.execute(query_regisseur, [(film_regisseur)])

	resultaat = cursor.fetchone()
	if resultaat:
		regisseur_id = resultaat[0]
		query_film = '''INSERT INTO Films (titel, release_jaar, genre, regisseur_id) 
				VALUES (?, ?, ?, ?)'''
		cursor.execute(query_film, (film_titel, film_release, film_genre, regisseur_id))
		dbconnectie.commit()
		print("De films die zich nu in de database bevinden zijn de volgende: ")
		toon_films_alle()
	else:
		print("De regisseur werd niet gevonden, maak eerst de regisseur aan")

	dbconnectie.close()

def voeg_regisseur_toe():
	dbconnectie, cursor = verkrijg_cursor()
	regisseur_naam = input("Geef de naam van de regisseur: ")
	regisseur_geboortejaar = int(input("Geef het geboortejaar van de regisseur: "))

	query = '''INSERT INTO Regisseurs (naam, geboorte_jaar) 
				VALUES (?, ?)'''

	cursor.execute(query, (regisseur_naam, regisseur_geboortejaar))

	dbconnectie.commit()
	print("De regisseur tabel werd uitgebreid, volgende gegevens zitten nu in de tabel: ")

	toon_regisseurs_alle()

	dbconnectie.close()