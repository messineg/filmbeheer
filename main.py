import sqlite3
from db.database import maak_connectie, maak_tabellen_voeg_data_toe
import json
import os
from functies.zoek_film import zoek_films_alle, zoek_film_vraag


if __name__ == '__main__':
	
	maak_connectie()
	maak_tabellen_voeg_data_toe()

	print("De eerste basis is uitgevoerd")

	acties = {
    "1": zoek_films_alle,
    "2": zoek_film_vraag
	}

	user_input= input("Geef een cijfer voor de functie die je wil laten uitvoeren: ")

	if user_input in acties:
		acties[user_input]()
	else:
   		print("Kies een ander cijfer")

	