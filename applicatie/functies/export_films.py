import sqlite3, csv, os
from config_laden import laad_config
from db.database import verkrijg_cursor

'''
Deze code bevat de functionaliteit om een rapport (csv) te exporteren.
1. Op basis van de config.json wordt opgehaald waar het rapport moet komen en hoe het moet noemen.
2. Alle films worden geëxporteerd en weggeschreven naar een csv-bestand
'''

def creatie_locatie_export():
	#Path maken waar de database moet komen
	config = laad_config()
	export_naam = config["export"]["naam"]
	export_locatie = config["export"]["locatie"]
	export_path = os.path.join(export_locatie, export_naam)

	if not os.path.exists(export_locatie):
		os.makedirs(export_locatie)

	return export_path

def exporteer_films():
	try:
		#Verkrijg het volledige pad naar het exportbestand
		export_path = creatie_locatie_export()
	
		#Query die moet dienen welke gegevens opgehaald moeten worden
		query = 'SELECT * FROM Films'

		#Kolomnamen die moeten dienen als header
		kolomnamen = ["id", "titel", "release_jaar", "genre", "regisseur_id"]

		with open(export_path, 'w', newline='') as bestand:
			#Indien bestand niet bestaat, het bestand aanmaken
			bestand_schrijven = csv.writer(bestand)

			#Schrijf de headers
			bestand_schrijven.writerow(kolomnamen)

			#Ophalen van de gegevens
			dbconnectie, cursor = verkrijg_cursor()
			cursor.execute(query)
			resultaten = cursor.fetchall()

			#Opgehaalde data wegschrijven naar het bestand
			bestand_schrijven.writerows(resultaten)

		print(f"Films zijn succesvol geëxporteerd naar {export_path}")
		dbconnectie.close()
	except Exception as error:
		print(f"Er deed zich een fout voor bij het exporteren: {error}")
		
	
	
