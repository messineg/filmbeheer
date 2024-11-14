import sqlite3
from db.database import maak_connectie
from db.klassen import Film, Regisseur

def zoek_films_alle():
	dbconnectie= maak_connectie()
	cursor = dbconnectie.cursor()
	cursor.execute('SELECT * FROM Films')
	
	for row in cursor:
		films = Film(row[0], row[1], row[2], row[3], row[4])
		films.beschrijf_film()

def zoek_film_vraag():
	dbconnectie= maak_connectie()
	cursor = dbconnectie.cursor()
	gezochte_film = input("Geef de titel van een film in:")
	cursor.execute('SELECT * FROM Films WHERE titel=?', (gezochte_film, ))
	
	for row in cursor:
		film = Film(row[0], row[1], row[2], row[3], row[4])
		film.beschrijf_film()