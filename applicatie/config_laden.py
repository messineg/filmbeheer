import json


def laad_config():
	with open("config.json") as bestand:
		config = json.load(bestand)
	return config
	

	