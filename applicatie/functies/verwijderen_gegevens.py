import sqlite3
from db.database import verkrijg_cursor
from db.klassen import Film, Regisseur
from functies.toon_gegevens import toon_films_alle

'''
Deze code dient voor het verwijderen van een film uit een database.
In deze code dient wel de volledige titel van een film worden ingegeven.
De gebruiker krijgt een melding wanneer een film succesvol werd verwijderd,
ofwel een melding dat de film niet werd gevonden in de database.
'''

def verwijder_film():
	#Ophalen van de connectie en de cursor
	dbconnectie, cursor = verkrijg_cursor()

	#Vraag de gebruiker welke film verwijderd mag worden en controleer of de titel niet leeg is
	film_titel = input("Welke film wenst u te verwijderen: ")
	if not film_titel:
		print("De titel van de film mag niet leeg zijn")
		return

	#Opsplitsten query en parameter om code leesbaarder te maken
	query = "DELETE FROM Films WHERE titel = ?"
	parameter = (film_titel, )

	#Ophalen en verwijderen van de film en erna tonen van welke films nu in de database zitten
	try:
		cursor.execute(query, parameter)
		gevonden_rijen = cursor.rowcount
		
	except sqlite3.Error as error:
		print(f"Database fout: {error}")

	if gevonden_rijen > 0:
		dbconnectie.commit()
		print(f"{film_titel} werd succesvol verwijderd.")
		toon_films_alle()
	else:
		print(f"{film_titel} werd niet gevonden in de database.")

	#Afsluiten van de connectie
	dbconnectie.close()
	