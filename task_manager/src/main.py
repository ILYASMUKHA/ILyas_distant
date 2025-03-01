
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.managers.task_manager import TaskManager

def main_menu():
    manager = TaskManager()
    while True:
        print("\n1. Добавить задачу")
        print("2. Показать все задачи")
        print("3. Изменить статус")
        print("4. Удалить задачу")
        print("5. Поиск задач")
        print("6. Выход")
        choice = input("Выберите опцию: ")
        if choice == '1':
            title = input("Введите название задачи: ")
            description = input("Введите описание задачи: ")
            manager.add_task(title, description)
        elif choice == '2':
            manager.list_tasks()
        elif choice == '3':
            task_id = int(input("Введите ID задачи: "))
            new_status = input("Введите новый статус: ")
            manager.update_task_status(task_id, new_status)
        elif choice == '4':
            task_id = int(input("Введите ID задачи: "))
            manager.delete_task(task_id)
        elif choice == '5':
            keyword = input("Введите ключевое слово: ")
            found_tasks = manager.search_tasks(keyword)
            for task in found_tasks:
                print(task)
        elif choice == '6':
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите опцию от 1 до 6.")

if __name__ == "__main__":
    main_menu()