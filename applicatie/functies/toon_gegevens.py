import sqlite3
from db.database import maak_connectie
from db.klassen import Film, Regisseur

def verkrijg_cursor():
	#Functie om niet telkens de code te moeten herhalen om de cursor op te halen
	dbconnectie= maak_connectie()
	cursor = dbconnectie.cursor()
	return dbconnectie, cursor

def toon_films_alle():
	
	dbconnectie, cursor = verkrijg_cursor()

	cursor.execute('SELECT * FROM Films')
	
	for row in cursor:
		films = Film(row[0], row[1], row[2], row[3], row[4])
		films.beschrijf_film()

	dbconnectie.close()

def toon_regisseurs_alle():
	dbconnectie, cursor = verkrijg_cursor()
	cursor.execute('SELECT * FROM Regisseurs')

	for row in cursor:
		regisseurs = Regisseur(row[0], row[1], row[2])
		regisseurs.beschrijf_regisseur()

	dbconnectie.close()