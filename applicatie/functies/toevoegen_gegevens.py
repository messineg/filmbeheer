import sqlite3
from db.database import verkrijg_cursor
from db.klassen import Film, Regisseur
from functies.toon_gegevens import toon_films_alle, toon_regisseurs_alle

'''
Dit bestand bevat alle functionaliteit om gegevens toe te voegen aan de tabel.
Bij het toevoegen van een film worden de gegevens van de film gevraagd.
Daarna is er een controle om te kijken of de opgegeven regisseur al bestaat in het systeem.
Indien niet, dan krijgt de gebruiker een melding te zien en zal de gebruiker eerst een regisseur moeten aanmaken.
Indien de regisseur wel wordt gevonden, wordt de film toegevoegd aan de database, 
en krijgt de gebruiker de lijst met alle films in het systeem te zien.
Wanneer de regisseur niet werd gevonden kan de gebruiker via het keuzemenu uit main.py kiezen om eerst de regisseur
toe te voegen. 
De gebruiker wordt gevraagd om de gegevens van de regisseur in te geven en erna wordt deze toegevoegd aan de tabel
'''

def voeg_film_toe():
	dbconnectie, cursor = verkrijg_cursor()

	#Vraag de gebruiker om de filmgegevens en controle op geldigheid input
	film_titel = input("Geef de titel van een film in: ")
	if not film_titel:
		print("De titel mag niet leeg zijn")
		return

	try:
		film_release = int(input("Geef releasejaar: "))
	except ValueError:
		print("Ongeldig releasejaar. Voer een geldig jaartal in.")
		return
	
	film_genre = input("Geef het genre in: ")
	
	film_regisseur = input("Geef regisseur: ")
	if not film_regisseur:
		print("De naam van de regisseur mag niet leeg zijn")
		return

	#Controle om te checken of de regisseur al bestaat
	query_regisseur = 'SELECT * FROM Regisseurs WHERE naam=?'
	try:
		cursor.execute(query_regisseur, [(film_regisseur)])
		resultaat = cursor.fetchone()
	except sqlite3.Error as error:
		print(f"Databasefout: {error}")
	
	#Wanneer de regisseur gevonden wordt, kan de film toegevoegd worden in de tabel
	if resultaat:
		regisseur_id = resultaat[0]
		query_film = '''INSERT INTO Films (titel, release_jaar, genre, regisseur_id) 
				VALUES (?, ?, ?, ?)'''
		#Inbouwen foutafhandeling, vooral voor wanneer bestaande film wordt toegevoegd
		try:
			cursor.execute(query_film, (film_titel, film_release, film_genre, regisseur_id))
			dbconnectie.commit()
			print(f"{film_titel} werd toegevoegd. De films die zich nu in de database bevinden zijn de volgende: ")
			toon_films_alle()
		except sqlite3.Error as error:
			print(f"Databasefout: {error}")	
	else:
		print("De regisseur werd niet gevonden, maak eerst de regisseur aan")

	#Afsluiten van de connectie
	dbconnectie.close()

def voeg_regisseur_toe():
	dbconnectie, cursor = verkrijg_cursor()

	#Opvragen van de gegevens en controle op geldigheid van input
	regisseur_naam = input("Geef de naam van de regisseur: ")
	if not regisseur_naam:
		print("De naam van de regisseur mag niet leeg zijn.")
		return
	try:
		regisseur_geboortejaar = int(input("Geef het geboortejaar van de regisseur: "))
	except ValueError:
		print("Ongeldig geboortejaar. Voer een geldig jaartal in.")
		return

	#Opsplitsen van de query zodat code leesbaarder wordt
	query = '''INSERT INTO Regisseurs (naam, geboorte_jaar) 
				VALUES (?, ?)'''

	#Foutafhandeling inbouwen, vooral voor poging om bestaande regisseur toe te voegen
	try:
		cursor.execute(query, (regisseur_naam, regisseur_geboortejaar))
		dbconnectie.commit()
		print(f"De regisseur tabel werd uitgebreid met {regisseur_naam}, volgende gegevens zitten nu in de tabel: ")
		toon_regisseurs_alle()
	except sqlite3.Error as error:
		print(f"Databasefout: {error}")

	#Afsluiten van de connectie
	dbconnectie.close()