from db.database import maak_connectie, setup_database
from functies.toon_gegevens import toon_films_alle, toon_regisseurs_alle
from functies.zoek_film import zoek_film_titel, zoek_film_regisseur
from functies.toevoegen_gegevens import voeg_film_toe, voeg_regisseur_toe
from functies.verwijderen_gegevens import verwijder_film
from functies.export_films import exporteer_films

'''
Dit is het centraal punt van de applicatie. 
Eerst wordt de database opgezet vanuit de code die werd geschreven in database.py.
Daarna krijgt de gebruiker te zien welke acties allemaal mogelijk zijn en kan de gebruiker op
basis van een cijfer kiezen welke functionaliteit hij wil starten.
'''

def main():
	setup_database()

	#Weergeven welke acties allemaal mogelijk zijn voor dit programma
	acties = {
    "1": ("Toon alle films", toon_films_alle),
    "2": ("Toon alle regisseurs", toon_regisseurs_alle),
    "3": ("Zoek een film op basis van de titel", zoek_film_titel),
    "4": ("Zoek een film op basis van de regisseur", zoek_film_regisseur),
    "5": ("Voeg een film toe", voeg_film_toe),
    "6": ("Voeg een regisseur toe", voeg_regisseur_toe),
    "7": ("Verwijder een film", verwijder_film),
    "8": ("Exporteer alle films", exporteer_films)
	}

	print("Beschikbare acties:")
	for key, (beschrijving, _) in acties.items():
		print(f"{key}: {beschrijving}")

	#Gebruiker vragen welke actie moet worden uitgevoerd
	user_input= input("Geef een cijfer voor de functie die je wil laten uitvoeren: ")

	#Lanceren van de functie of gebruiker er op wijzen dat een geldig cijfer moet gekozen worden
	if user_input in acties:
		acties[user_input][1]()
	else:
   		print("Ongeldige keuze, probeer het opnieuw")

if __name__ == '__main__':
	
	main()
	

	