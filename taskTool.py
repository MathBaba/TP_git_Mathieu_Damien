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


def supprimer_tache_json(nom_fichier, titre_tache):
    try:
        with open(nom_fichier, 'r') as fichier:
            liste_taches = json.load(fichier)
    except FileNotFoundError:
        print(f"Le fichier {nom_fichier} n'existe pas.")
        return

    if titre_tache in liste_taches:
        del liste_taches[titre_tache]
        print(f"Tâche '{titre_tache}' supprimée.")
    else:
        print(f"Tâche '{titre_tache}' non trouvée dans la liste.")

    with open(nom_fichier, 'w') as fichier:
        json.dump(liste_taches, fichier, indent=2)

    return liste_taches


def marquer_tache_terminee(nom_fichier, titre_tache):
    try:
        with open(nom_fichier, 'r') as fichier:
            liste_taches = json.load(fichier)
    except FileNotFoundError:
        print(f"Le fichier {nom_fichier} n'existe pas.")
        return

    if titre_tache in liste_taches:
        liste_taches[titre_tache]["completee"] = True
        print(f"Tâche '{titre_tache}' marquée comme terminée.")
    else:
        print(f"Tâche '{titre_tache}' non trouvée dans la liste.")

    with open(nom_fichier, 'w') as fichier:
        json.dump(liste_taches, fichier, indent=2)

    return liste_taches

