import sqlite3, os
from config_laden import laad_config

'''
Dit bestand dient om de hele database op te zetten:
1. Creatie van de locatie op basis van wat er werd geconfigureerd in de config.json.
2. Maken van connectie, zodat deze ook in andere bestanden kan worden gebruikt.
3. Verkrijgen van cursor, idem zoals bij het maken van de connectie.
4. Opzetten van de initiële database met data.
'''

def creatie_locatie_database():
	#Path maken waar de database moet komen
	config = laad_config()
	db_naam = config["database"]["naam"]
	db_locatie = config["database"]["locatie"]
	db_path = os.path.join(db_locatie, db_naam)

	if not os.path.exists(db_locatie):
		os.makedirs(db_locatie)

	return db_path

def maak_connectie():
	#Ophalen database naam en locatie om te kunnen verbinden
	db_path = creatie_locatie_database()

	#Verbinding maken met de database
	try:
		dbconnectie = sqlite3.connect(db_path)
		print("Verbonden met database")
		return dbconnectie
	except sqlite3.Error as error:
		print(f"Er deed zich een fout voor: {error}")
	

def verkrijg_cursor():
	#Functie om niet telkens de code te moeten herhalen om de cursor op te halen
	dbconnectie= maak_connectie()
	cursor = dbconnectie.cursor()

	return dbconnectie, cursor

def setup_database():
	dbconnectie, cursor = verkrijg_cursor()

	#Controleer of de setup al is uitgevoerd
	cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Films'")
	if cursor.fetchone() is not None:
		print("Database is al ingesteld. Setup wordt overgeslagen")
		dbconnectie.close()
		return

	#Eerst creatie van Regisseurs, aangezien we in de Films tabel een FK naar deze tabel zullen nodig hebben
	cursor.execute('''CREATE TABLE IF NOT EXISTS Regisseurs (
					id INTEGER PRIMARY KEY AUTOINCREMENT,
					naam TEXT,
					geboorte_jaar INTEGER,
					UNIQUE(naam, geboorte_jaar))''')

	#Creatie van de Film tabel
	cursor.execute('''CREATE TABLE IF NOT EXISTS Films (
					id INTEGER PRIMARY KEY AUTOINCREMENT, 
					titel TEXT,   
					release_jaar INTEGER, 
					genre TEXT,
					regisseur_id INTEGER,
					FOREIGN KEY (regisseur_id) REFERENCES Regisseurs (id),
					UNIQUE(titel, release_jaar, regisseur_id) )''')

	#Voeg regisseurs data toe aan de tabel
	regisseurs_data = [('Christopher Nolan', 1970),('Steven Spielberg', 1946),('Quentin Tarantino', 1963),('Martin Scorsese', 1942),('James Cameron', 1954)]
	cursor.executemany('INSERT OR IGNORE INTO Regisseurs (naam, geboorte_jaar) VALUES (?, ?)', regisseurs_data)  
	
	#Voeg films toe en zoek naar de id van de regisseur op basis van de naam
	cursor.execute('''
        INSERT OR IGNORE INTO Films (titel, release_jaar, genre, regisseur_id)
        VALUES 
            ('Inception', 2010, 'Science Fiction', (SELECT id FROM Regisseurs WHERE naam = 'Christopher Nolan')),
            ('Schindler List', 1993, 'Drama', (SELECT id FROM Regisseurs WHERE naam = 'Steven Spielberg')),
            ('Pulp Fiction', 1994, 'Crime', (SELECT id FROM Regisseurs WHERE naam = 'Quentin Tarantino')),
            ('Goodfellas', 1990, 'Crime', (SELECT id FROM Regisseurs WHERE naam = 'Martin Scorsese')),
            ('Avatar', 2009, 'Action', (SELECT id FROM Regisseurs WHERE naam = 'James Cameron')),
            ('The Departed', 2006, 'Crime',(SELECT id FROM Regisseurs WHERE naam = 'Martin Scorsese'))
        ''')


	#Gegevens doorvoeren en connectie afsluiten
	dbconnectie.commit()
	print("Database setup is voltooid.")
	dbconnectie.close()

