import sqlite3

def maak_connectie():
	#Verbinding maken met de database
	try:
		dbconnectie = sqlite3.connect("filmbeheer.db")
		print("Verbonden met database")
	except sqlite3.Error as error:
		print(f"Er deed zich een fout voor: {error}")
	return dbconnectie

def maak_tabellen():
	connectie = maak_connectie()
	cursor = connectie.cursor()
	#Eerst creatie van Regisseurs, aangezien we in de Films tabel een FK naar deze tabel zullen nodig hebben
	cursor.execute('''CREATE TABLE IF NOT EXISTS Regisseurs (
					id INTEGER PRIMARY KEY AUTOINCREMENT,
					naam TEXT,
					geboorte_jaar INTEGER)''')

	#Creatie van de Film tabel
	cursor.execute('''CREATE TABLE IF NOT EXISTS Films (
					id INTEGER PRIMARY KEY AUTOINCREMENT, 
					titel TEXT,   
					release_jaar INTEGER, 
					genre TEXT,
					regisseur_id INTEGER,
					FOREIGN KEY (regisseur_id)
						REFERENCES Regisseurs (id) )''')

	print("Tabellen werden aangemaakt")

maak_tabellen() 