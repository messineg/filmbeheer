import sqlite3
from db.database import maak_connectie

def zoek_films_alle():
	dbconnectie= maak_connectie()
	cursor = dbconnectie.cursor()
	cursor.execute('SELECT * FROM Films')
	for row in cursor:
		print(row)

def zoek_film_vraag():
	dbconnectie= maak_connectie()
	cursor = dbconnectie.cursor()
	gezochte_film = input("Geef de titel van een film in:")
	cursor.execute('SELECT * FROM Films WHERE titel=?', (gezochte_film, ))
	for row in cursor:
		print(row)