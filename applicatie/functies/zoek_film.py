import sqlite3
from db.database import verkrijg_cursor
from db.klassen import Film, Regisseur

def zoek_film_titel():
	#Ophalen van de db connectie en cursor
	dbconnectie, cursor= verkrijg_cursor()

	#Input vragen aan de gebruiker welke film er gezocht moet worden
	gezochte_film = input("Geef de titel van een film in: ")

	#Opsplitsen query en parameter om de code leesbaarder te maken
	query = '''SELECT Films.id, Films.titel, Films.release_jaar, Films.genre, 
		Regisseurs.naam, Regisseurs.geboorte_jaar 
		FROM Films
		JOIN Regisseurs ON Films.regisseur_id = Regisseurs.id 
		WHERE Films.titel LIKE ?'''
	parameter = (f"%{gezochte_film}%", )

	#Uitvoeren van de query en ophalen resultaten met foutafhandeling
	try:
		cursor.execute(query, parameter)
		resultaten = cursor.fetchall()
	except sqlite3.Error as error:
		print(f"Er deed zich een error voor bij het ophalen van de gegevens: {error}")

	#Weergave van de resultaten
	if resultaten:
		print(f"{len(resultaten)} resultaat/resultaten gevonden:")
		for row in resultaten:
			film = Film(row[0], row[1], row[2], row[3], row[4])
			regisseur = Regisseur(row[4], row[4], row[5])
			print("Filmgegevens:")
			film.beschrijf_film()
			print("Regisseurgegevens:")
			regisseur.beschrijf_regisseur()
	else:
		print("Geen films gevonden op basis van de zoekopdracht")
	
	#Afsluiten van de connectie
	dbconnectie.close()

def zoek_film_regisseur():
	#Ophalen van de db connectie en cursor
	dbconnectie, cursor= verkrijg_cursor()
	
	#Input vragen aan de gebruiker van welke regisseur de films gezocht worden
	gezochte_regisseur = input("Geef de naam van een regisseur in: ")

	#Opsplitsen query en parameter om de code leesbaarder te maken
	query = '''SELECT Films.id, Films.titel, Films.release_jaar, Films.genre, 
		Regisseurs.naam, Regisseurs.geboorte_jaar 
		FROM Films
		JOIN Regisseurs ON Films.regisseur_id = Regisseurs.id 
		WHERE Regisseurs.naam LIKE ?'''
	parameter = (f"%{gezochte_regisseur}%", )

	#Uitvoeren van de query en ophalen resultaten met foutafhandeling
	try:
		cursor.execute(query,parameter)
		resultaten = cursor.fetchall()
	except sqlite3.Error as error:
		print(f"Er deed zich een error voor bij het ophalen van de gegevens: {error}")
	
	#Weergave van de resultaten
	if resultaten:
		print(f"{len(resultaten)} resultaat/resultaten gevonden:")
		for row in resultaten:
			film = Film(row[0], row[1], row[2], row[3], row[4])
			regisseur = Regisseur(row[4], row[4], row[5])
			print("Filmgegevens:")
			film.beschrijf_film()
			print("Regisseurgegevens:")
			regisseur.beschrijf_regisseur()
	else:
		print("Geen resultaten gevonden")

	#Afsluiten van de connectie
	dbconnectie.close()