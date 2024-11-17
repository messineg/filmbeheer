import sqlite3
from db.database import maak_connectie, maak_tabellen_voeg_data_toe
import json
import os
from functies.zoek_gegevens import zoek_films_alle, zoek_film_vraag

def main():
	maak_connectie()
	maak_tabellen_voeg_data_toe()

	print("De eerste basis is uitgevoerd")

	acties = {
    "1": ("Toon alle films", zoek_films_alle),
    "2": ("Zoek een film", zoek_film_vraag)
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
	

	