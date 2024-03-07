from taskTool import add_task, delete_task, complete_task, save_to_json, load_from_json

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
    else:
        print("Choix invalide. Quitter le programme.")

def create_new_tasks():
    tasks = {}
    
    add_task(tasks, 'task1', 'Faire quelque chose', '2024-03-15')
    add_task(tasks, 'task2', 'Terminer le TP', '2024-03-20')

    return tasks

if __name__ == "__main__":
    main()


def create_new_tasks():
    tasks = {}
    add_task(tasks, 'task1', 'Faire quelque chose', '2024-03-15')
    add_task(tasks, 'task2', 'Terminer le TP', '2024-03-20')

    save_option = input("Voulez-vous sauvegarder la liste de tâches ? (oui/non): ").lower()
    if save_option == 'oui':
        save_to_json(tasks, 'tasks_data.json')

    return tasks

