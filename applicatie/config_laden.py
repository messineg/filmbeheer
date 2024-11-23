import json
import os

def laad_config():
	#Opbouw van path waar config.json te vinden moet zijn
	huidige_map = os.path.dirname(os.path.abspath(__file__))
	pad_naar_config = os.path.join(huidige_map,"..","config.json")

	#config.json inladen met ingebouwde foutafhandeling wanneer bestand niet gevonden wordt of er zich een algemene fout voordoet
	try:
		with open(pad_naar_config, "r") as bestand:
			config = json.load(bestand)
		return config
	except FileNotFoundError:
		print(f"Het bestand config.json werd niet gevonden op pad: {pad_naar_config}")
	except Exception as error:
		print(f"Er deed zich een fout voor: {error}")

	