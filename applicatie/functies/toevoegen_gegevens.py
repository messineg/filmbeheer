import sqlite3
from db.database import verkrijg_cursor
from db.klassen import Film, Regisseur
from functies.toon_gegevens import toon_films_alle

def voeg_film_toe():
	dbconnectie, cursor = verkrijg_cursor()

	
	filmtitel = input("Geef de titel van een film in: ")
	filmrelease = input("Geef releasejaar: ")
	filmgenre = input("Geef het genre in: ")
	filmregisseur = input("Geef regisseur:")

	query = '''INSERT INTO Films (titel, release_jaar, genre, regisseur_id) VALUES (?, ?, ?, ?)'''

	
	cursor.execute(query, (filmtitel, filmrelease, filmgenre, filmregisseur))

	dbconnectie.commit()
	toon_films_alle()