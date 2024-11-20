import sqlite3
from db.database import verkrijg_cursor
from db.klassen import Film, Regisseur

def toon_films_alle():
	
	dbconnectie, cursor = verkrijg_cursor()
	
	#Definieer de query om code leesbaarder te maken
	query = 'SELECT * FROM Films'
	
	#Ophalen van resultaten met foutafhandeling
	try:
		cursor.execute(query)
		resultaten = cursor.fetchall()
	except sqlite3.Error as error:
		print(f"Er trad een fout op bij het ophalen van de gegevens: {error}")
	
	#Controle of er resultaten gevonden worden en tonen van deze resultaten
	if resultaten:
		for row in resultaten:
			films = Film(row[0], row[1], row[2], row[3], row[4])
			films.beschrijf_film()
	else:
		print("Er werden geen films gevonden")
	
	#Afsluiten connectie
	dbconnectie.close()

def toon_regisseurs_alle():
	dbconnectie, cursor = verkrijg_cursor()
	
	#Definieer de query om code leesbaarder te maken
	query = 'SELECT * FROM Regisseurs'

	#Ophalen van resultaten met foutafhandeling
	try:
		cursor.execute(query)
		resultaten = cursor.fetchall()
	except sqlite3.Error as error:
		print(f"Er trad een fout op bij het ophalen van de gegevens: {error}")

	#Controle of er resultaten gevonden worden en tonen van deze resultaten
	if resultaten:
		for row in resultaten:
			regisseurs = Regisseur(row[0], row[1], row[2])
			regisseurs.beschrijf_regisseur()
	else:
		print("Er werden geen regisseurs gevonden")

	#Afsluiten van connectie
	dbconnectie.close()