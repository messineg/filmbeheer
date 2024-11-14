class Film():
	def __init__(self, id, titel, release_jaar, genre, regisseur):
		self.id = id
		self.titel = titel
		self.release_jaar = release_jaar
		self.genre = genre
		self.regisseur = regisseur

	def beschrijf_film(self):
		print(f"""
Titel: {self.titel};
Releasejaar: {self.release_jaar}; 
Genre: {self.genre}""")


class Regisseur():
	def __init__(self, id, naam, geboorte_jaar):
		self.id = id
		self.naam = naam
		self.geboorte_jaar = geboorte_jaar

	def beschrijf_regisseur(self):
		print(f"Naam: {self.naam}; Geboortejaar = {self.geboorte_jaar}")
