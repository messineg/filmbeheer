import sqlite3
from db.database import verkrijg_cursor
from db.klassen import Film, Regisseur

def toon_films_alle():
	
	dbconnectie, cursor = verkrijg_cursor()
	query = 'SELECT * FROM Films'
	cursor.execute(query)
	resultaten = cursor.fetchall()
	
	if resultaten:
		for row in resultaten:
			films = Film(row[0], row[1], row[2], row[3], row[4])
			films.beschrijf_film()
	else:
		print("Er werden geen films gevonden")
	dbconnectie.close()

def toon_regisseurs_alle():
	dbconnectie, cursor = verkrijg_cursor()
	
	query = 'SELECT * FROM Regisseurs'

	cursor.execute(query)
	resultaten = cursor.fetchall()

	if resultaten:
		for row in resultaten:
			regisseurs = Regisseur(row[0], row[1], row[2])
			regisseurs.beschrijf_regisseur()
	else:
		print("Er werden geen regisseurs gevonden")

	dbconnectie.close()