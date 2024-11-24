import sqlite3
from db.database import verkrijg_cursor
from db.klassen import Film, Regisseur

'''
Deze code voorziet het tonen van de gegevens die op het moment van het aanroepen van de functies beschikbaar
zijn in het systeem. 
Er is een functie die alle films ophaalt en deze weergeeft voor de gebruiker.
Daarnaast is er ook een functie die alle regisseurs gaat weergeven.
De functie om alle films weer te geven, zal ook dienen om na het toevoegen of verwijderen te tonen 
wat er allemaal in de database zit. Zo krijgt de gebruiker onmiddellijk feedback van zijn/haar actie.
'''

def toon_films_alle():
	#Ophalen van de connectie en de cursor
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
			print(films)
	else:
		print("Er werden geen films gevonden")
	
	#Afsluiten connectie
	dbconnectie.close()

def toon_regisseurs_alle():
	#Ophalen van de connectie en de cursor
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
			print(regisseurs)
	else:
		print("Er werden geen regisseurs gevonden")

	#Afsluiten van connectie
	dbconnectie.close()