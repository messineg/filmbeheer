import sqlite3
import os

def maak_connectie():
	#Path maken waar de database moet komen
	if not os.path.exists('data'):
		os.makedirs('data')

	#Verbinding maken met de database
	try:
		dbconnectie = sqlite3.connect("data/filmbeheer.db")
		print("Verbonden met database")
	except sqlite3.Error as error:
		print(f"Er deed zich een fout voor: {error}")
	return dbconnectie

def maak_tabellen_voeg_data_toe():
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

	#Voeg regisseurs data toe aan de tabel
	regisseurs_data = [('Christopher Nolan', 1970),('Steven Spielberg', 1946),('Quentin Tarantino', 1963),('Martin Scorsese', 1942),('James Cameron', 1954)]
	cursor.executemany('INSERT INTO Regisseurs (naam, geboorte_jaar) VALUES (?, ?)', regisseurs_data)  
	
	print("Initiële data voor regisseurs werd toegevoegd.")
	
	#Voeg films toe en zoek naar de id van de regisseur op basis van de naam
	cursor.execute('''
        INSERT INTO Films (titel, release_jaar, genre, regisseur_id)
        VALUES 
            ('Inception', 2010, 'Science Fiction', (SELECT id FROM Regisseurs WHERE naam = 'Christopher Nolan')),
            ('Schindler List', 1993, 'Drama', (SELECT id FROM Regisseurs WHERE naam = 'Steven Spielberg')),
            ('Pulp Fiction', 1994, 'Crime', (SELECT id FROM Regisseurs WHERE naam = 'Quentin Tarantino')),
            ('Goodfellas', 1990, 'Crime', (SELECT id FROM Regisseurs WHERE naam = 'Martin Scorsese')),
            ('Avatar', 2009, 'Action', (SELECT id FROM Regisseurs WHERE naam = 'James Cameron'))
        ''')


	connectie.commit()
	connectie.close()

