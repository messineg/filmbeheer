# Filmbeheer Applicatie

Een Python-project voor het beheren van films en regisseurs, inclusief functionaliteiten voor toevoegen, zoeken, verwijderen en exporteren naar een CSV-rapport.

## Over het project

De filmbeheer applicatie werd geschreven in opdracht voor het vak Programming in Python.

Het biedt een eenvoudige manier om een database van films en regisseurs te beheren. Gebruikers kunnen nieuwe films toevoegen, bestaande films verwijderen, en gegevens exporteren naar een CSV-bestand. 

De applicatie maakt gebruik van een kleine SQLite database waar de gegevens bewaard worden in twee tabellen, namelijk Films en Regisseurs.

## Functies

- Automatische initialisatie van de SQLite-database
- Weergave van alle films en regisseurs in de database
- Zoeken op titel of regisseur
- Verwijderen van films uit de database
- Exporteren van alle films naar een CSV-rapport

## Installatie

1. Ga binnen de terminal naar de map waar je het project wenst te installeren:
```
git clone https://github.com/messineg/filmbeheer.git
```

2. Ga naar de map van het project:
```
cd filmbeheer
```

3. Maak een virtuele omgeving aan:
```
python -m venv venv
```

4. Activeer de virtuele omgeving:
```
venv\Scripts\activate (voor Windows)
source venv/bin/activate (voor Mac OS)
```

5. Installeer de benodigde Python-pakketten
```
pip install -r requirements.txt
```

6. Configuratie instellen
- Open config.example.json
- Indien gewenst geef je de data of export map een andere naam
- Indien gewenst geef je de database of export file een andere naam 
- Sla het bestand op als config.json

## Gebruik

1. Ga naar de applicatie map binnen het project

```
cd applicatie
```

2. Start de applicatie
```
python main.py
```

3. Kies een optie uit het menu
- 1: Toon alle films
- 2: Toon alle regisseurs
- 3: Zoek films op titel
- 4: Zoek films op regisseur
- 5: Voeg een film toe
- 6: Voeg een regisseur toe
- 7: Verwijder een film
- 8: Exporteer films naar CSV

4. Volg de instructies bij het uitvoeren van een functie

