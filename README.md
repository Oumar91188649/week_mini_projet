Mini-projet de gestion d'un hôtel
 Importation de la base de données
Le fichier hotel.sql fourni par l'enseignant a été importé
dans DB Browser for SQLite afin de créer la base hotel.db.
Le script contient déjà les instructions de création des tables
et les données initiales. Il n'a pas été réécrit.
 Organisation des fichiers- 
 db.py : connexion à la base SQLite et activation des clés étrangères.- 
 models.py : fonctions de consultation et de gestion des réservations.- 
 main.py : point d'entrée du programme.- 
 verification_models.py : tests simples des fonctions.- hotel.sql : script SQL original fourni.
 Chemin de la base
Le chemin est construit avec Path(__file__).resolve().parent.
Il dépend de l'emplacement de db.py et non du dossier depuis
lequel la commande Python est lancée. Le programme retrouve
donc hotel.db même si le terminal est ouvert ailleurs.
