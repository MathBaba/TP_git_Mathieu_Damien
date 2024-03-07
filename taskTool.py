import json

def ajouter_tache_json(nom_fichier, titre, description, date_echeance):
   
    try:
        
        with open(nom_fichier, 'r') as fichier:
            liste_taches = json.load(fichier)
    except FileNotFoundError:
        
        liste_taches = {}


    nouvelle_tache = {
        "titre": titre,
        "description": description,
        "date_echeance": date_echeance,
        "completee": False 
    }


    liste_taches[titre] = nouvelle_tache

   
    with open(nom_fichier, 'w') as fichier:
        json.dump(liste_taches, fichier, indent=2)

    return liste_taches



ajouter_tache_json("")
