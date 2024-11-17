import json
import os

def laad_config():
	huidige_map = os.path.dirname(os.path.abspath(__file__))
	pad_naar_config = os.path.join(huidige_map,"..","config.json")

	with open(pad_naar_config) as bestand:
		config = json.load(bestand)
	return config

	