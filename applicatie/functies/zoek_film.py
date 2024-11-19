import sqlite3
from db.database import verkrijg_cursor
from db.klassen import Film, Regisseur

def zoek_film_titel():
	dbconnectie, cursor= verkrijg_cursor()

	gezochte_film = input("Geef de titel van een film in: ")
	query = '''SELECT Films.id, Films.titel, Films.release_jaar, Films.genre, 
		Regisseurs.naam, Regisseurs.geboorte_jaar 
		FROM Films
		JOIN Regisseurs ON Films.regisseur_id = Regisseurs.id 
		WHERE Films.titel LIKE ?'''

	parameter = (f"%{gezochte_film}%", )
	
	cursor.execute(query, parameter)
	
	resultaten = cursor.fetchall()

	if resultaten:
		for row in resultaten:
			print("Resultaat gevonden")
			film = Film(row[0], row[1], row[2], row[3], row[4])
			regisseur = Regisseur(row[4], row[4], row[5])
			print("Filmgegevens:")
			film.beschrijf_film()
			print("Regisseurgegevens:")
			regisseur.beschrijf_regisseur()
	else:
		print("Geen films gevonden op basis van de zoekopdracht")
	
	dbconnectie.close()

def zoek_film_regisseur():
	dbconnectie, cursor= verkrijg_cursor()
	
	gezochte_regisseur = input("Geef de naam van een regisseur in: ")
	query = '''SELECT Films.id, Films.titel, Films.release_jaar, Films.genre, 
		Regisseurs.naam, Regisseurs.geboorte_jaar 
		FROM Films
		JOIN Regisseurs ON Films.regisseur_id = Regisseurs.id 
		WHERE Regisseurs.naam LIKE ?'''
	parameter = (f"%{gezochte_regisseur}%", )

	cursor.execute(query,parameter)

	resultaten = cursor.fetchall()
	
	if resultaten:
		for row in resultaten:
			film = Film(row[0], row[1], row[2], row[3], row[4])
			regisseur = Regisseur(row[4], row[4], row[5])
			print("Filmgegevens:")
			film.beschrijf_film()
			print("Regisseurgegevens:")
			regisseur.beschrijf_regisseur()
	else:
		print("Geen resultaten gevonden")

	dbconnectie.close()