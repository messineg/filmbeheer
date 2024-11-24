'''
Definiëren van de twee klasses op basis van de kolommen die werden gedefinieerd bij het opzetten van de database.
Telkens ook een __str__ functie om de weergave van de data mooier te maken.
'''

class Film():
	def __init__(self, id, titel, release_jaar, genre, regisseur):
		self.id = id
		self.titel = titel
		self.release_jaar = release_jaar
		self.genre = genre
		self.regisseur = regisseur

	def __str__(self):
		return f"Titel: {self.titel}\nReleasejaar: {self.release_jaar}\nGenre: {self.genre}"


class Regisseur():
	def __init__(self, id, naam, geboorte_jaar):
		self.id = id
		self.naam = naam
		self.geboorte_jaar = geboorte_jaar

	def __str__(self):
		 return f"Naam: {self.naam}\nGeboortejaar: {self.geboorte_jaar}"
