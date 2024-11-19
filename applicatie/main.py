from db.database import maak_connectie, setup_database
from functies.toon_gegevens import toon_films_alle, toon_regisseurs_alle
from functies.zoek_film import zoek_film_titel, zoek_film_regisseur
from functies.toevoegen_gegevens import voeg_film_toe, voeg_regisseur_toe

def main():
	setup_database()

	acties = {
    "1": ("Toon alle films", toon_films_alle),
    "2": ("Toon alle regisseurs", toon_regisseurs_alle),
    "3": ("Zoek een film op basis van de titel", zoek_film_titel),
    "4": ("Zoek een film op basis van de regisseur", zoek_film_regisseur),
    "5": ("Voeg een film toe", voeg_film_toe),
    "6": ("Voeg een regisseur toe", voeg_regisseur_toe)
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
	

	