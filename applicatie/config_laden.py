import json
import os

def laad_config():
	#Opbouw van path waar config.json te vinden moet zijn
	huidige_map = os.path.dirname(os.path.abspath(__file__))
	pad_naar_config = os.path.join(huidige_map,"..","config.json")

	with open(pad_naar_config) as bestand:
		config = json.load(bestand)
	return config

	