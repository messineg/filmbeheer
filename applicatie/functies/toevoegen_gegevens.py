import sqlite3
from db.database import verkrijg_cursor
from db.klassen import Film, Regisseur
from functies.toon_gegevens import toon_films_alle, toon_regisseurs_alle

def voeg_film_toe():
	dbconnectie, cursor = verkrijg_cursor()

	
	filmtitel = input("Geef de titel van een film in: ")
	filmrelease = int(input("Geef releasejaar: "))
	filmgenre = input("Geef het genre in: ")
	filmregisseur = input("Geef regisseur:")

	query = '''INSERT INTO Films (titel, release_jaar, genre, regisseur_id) 
				VALUES (?, ?, ?, ?)'''

	
	cursor.execute(query, (filmtitel, filmrelease, filmgenre, filmregisseur))

	dbconnectie.commit()
	print("De films die zich nu in de database bevinden zijn de volgende: ")
	toon_films_alle()

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