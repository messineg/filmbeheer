import sqlite3
from db.database import maak_connectie, maak_tabellen_voeg_data_toe


if __name__ == '__main__':
	maak_connectie()
	maak_tabellen_voeg_data_toe()

	print("De eerste basis is uitgevoerd")