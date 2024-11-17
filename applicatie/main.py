import sqlite3
from db.database import maak_connectie, setup_database
import json
import os
from functies.toon_gegevens import toon_films_alle, toon_regisseurs_alle
from functies.zoek_film import zoek_film_vraag

def main():
	maak_connectie()
	setup_database()

	print("De eerste basis is uitgevoerd")

	acties = {
    "1": ("Toon alle films", toon_films_alle),
    "2": ("Toon alle regisseurs", toon_regisseurs_alle),
    "3": ("Zoek een film", zoek_film_vraag)
	}

	print("Beschikbare acties:")
	for key, (beschrijving, _) in acties.items():
		print(f"{key}: {beschrijving}")

	user_input= input("Geef een cijfer voor de functie die je wil laten uitvoeren: ")

	if user_input in acties:
		acties[user_input][1]()
	else:
   		print("Kies een ander cijfer")

if __name__ == '__main__':
	
	main()
	

	