import os



TODO_FILE = "spravy.txt"

def show_tasks():
    """"ВиВодить усі справи"""
    try:
        with open(TODO_FILE, 'r',encoding='utf-8') as file:
            tasks = file.readlines()
    except FileNotFoundError:
        print(" WORK FILE DOESNT EXIST. NO WORK TO DO!")
        return

    if not tasks:
        print("TODO FILE EMPTY. YOUR FREE!")
    else:
        print("\n TO DO FOR TODAY")
        for i, task in enumerate(tasks, 1):

            print(f"{i}. {tasks.strip()}")
        print("-" *  25)
def add_task():
    new_task = input(" What job to add to the list? (For example: WALK YOUR DOG): ")
    if new_task:
        
        with open(TODO_FILE, 'a', encoding='utf-8') as file:
            file.write(new_task + "\n")
        print(f" TODO '{new_task}' ADDED!")
    else:
        print("YOU DIDNT WRITE ANYTHING. Task not added.")


def clear_tasks():


    if os.path.exists(TODO_FILE):
        confirm = input(" ETENTION! DO YOU REALLY WANT TO CLEAR ALL OF THE TASKS???????????????????? (yes/no): ").lower()
        if confirm == 'yes':
            with open(TODO_FILE, 'w', encoding='utf-8') as file:
                file.write("")
            print(" All tasks succsesfully deleted! (file cleared).")
        else:
            print("CLEARING CANCELED.")
    else:
        print("Task File non existing, NOTHING TO CLEAR!!.")

def todo_list_app():
    print("\n* ПРОГРАМА ОБЛІКУ СПРАВ (TO-DO LIST)")
    while True:
        print("\n --- MEHI0 --- ")
        print ("1 - Показати всі справи")
        print ("2 - Додати нову справу")
        print ( "3 - Очистити всі справи")
        print("4 - Вийти з програми")

        choice = input("Обери дію (1-4):")
                       
        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            clear_tasks()
        elif choice == '4':
            print("Дякую за використання програми! До зустрічі.")
            break
        else:
            print("XНевірний вибір. Спробуй ще раз (1, 2, 3, або 4).")
if __name__ == "__main__":
      todo_list_app()

