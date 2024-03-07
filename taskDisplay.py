# taskDisplay.py

import json
import os

def save_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=2)

def load_from_json(filename):
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
    return data

def add_task(tasks, task_name, description, deadline):
    tasks[task_name] = {
        'description': description,
        'deadline': deadline,
        'status': 'À faire'
    }

def delete_task(tasks, task_name):
    if task_name in tasks:
        del tasks[task_name]

def complete_task(tasks, task_name):
    if task_name in tasks:
        tasks[task_name]['status'] = 'Terminée'

def main():
    print("Que souhaitez-vous faire ?")
    print("1. Créer une nouvelle liste de tâches")
    print("2. Charger une liste de tâches existante")
    choice = input("Choisissez 1 ou 2 : ")

    if choice == '1':
        tasks = create_new_tasks()
        save_option = input("Voulez-vous sauvegarder la liste de tâches ? (oui/non): ").lower()
        if save_option == 'oui':
            save_to_json(tasks, 'tasks_data.json')
    elif choice == '2':
        tasks = load_from_json('tasks_data.json')
    
    # Ajouter, supprimer et marquer une tâche comme complète
    manage_tasks(tasks)

def create_new_tasks():
    tasks = {}
    add_task(tasks, 'task1', 'Faire quelque chose', '2024-03-15')
    add_task(tasks, 'task2', 'Terminer le TP', '2024-03-20')
    return tasks

def manage_tasks(tasks):
    while True:
        print("\nGestion des tâches :")
        print("1. Ajouter une tâche")
        print("2. Supprimer une tâche")
        print("3. Marquer une tâche comme complète")
        print("4. Quitter")
        
        choice = input("Choisissez une action (1-4) : ")
        
        if choice == '1':
            task_name = input("Nom de la tâche : ")
            description = input("Description de la tâche : ")
            deadline = input("Date limite de la tâche : ")
            add_task(tasks, task_name, description, deadline)
        elif choice == '2':
            task_name = input("Nom de la tâche à supprimer : ")
            delete_task(tasks, task_name)
        elif choice == '3':
            task_name = input("Nom de la tâche à marquer comme complète : ")
            complete_task(tasks, task_name)
        elif choice == '4':
            save_option = input("Voulez-vous sauvegarder la liste de tâches ? (oui/non): ").lower()
            if save_option == 'oui':
                save_to_json(tasks, 'tasks_data.json')
            break
        else:
            print("Choix invalide. Veuillez choisir une option valide.")

if __name__ == "__main__":
    main()

