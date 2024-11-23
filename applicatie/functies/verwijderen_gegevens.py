import sqlite3
from db.database import verkrijg_cursor
from db.klassen import Film, Regisseur
from functies.toon_gegevens import toon_films_alle

def verwijder_film():
	#Ophalen van de connectie en de cursor
	dbconnectie, cursor = verkrijg_cursor()

	#Vraag de gebruiker welke film verwijderd mag worden
	film_titel = input("Welke film wenst u te verwijderen: ")

	#Opsplitsten query en parameter om code leesbaarder te maken
	
	parameter = (film_titel, )

	#Ophalen en verwijderen van de film en erna tonen van welke films nu in de database zitten
	try:
		cursor.execute(query, parameter)
		if cursor.rowcount > 0:
			dbconnectie.commit()
			print(f"{film_titel} werd succesvol verwijderd.")
			toon_films_alle()
		else:
			print(f"{film_titel} werd niet gevonden in de database.")
		
	except sqlite3.Error as error:
		print(f"Er deed zich een foutmelding voor bij het verwijderen van de film: {error}")

	