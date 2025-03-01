from src.models.task import Task
from src.utils.db import save_tasks_to_db, load_tasks_from_db

class TaskManager:
    def __init__(self, db_path='tasks.db'):
        """
        Инициализирует менеджер задач.
        :param db_path: Путь к базе данных (по умолчанию 'tasks.db').
        """
        self.db_path = db_path
        self.tasks = []
        self.load_tasks_from_db()

    def add_task(self, title, description):
        if not title:
            raise ValueError("Название задачи не может быть пустым")
        task_id = len(self.tasks) + 1
        task = Task(task_id, title, description)
        self.tasks.append(task)
        self.save_tasks_to_db()

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        self.save_tasks_to_db()

    def update_task_status(self, task_id, new_status):
        for task in self.tasks:
            if task.task_id == task_id:
                task.status = new_status
                break
        self.save_tasks_to_db()

    def list_tasks(self):
        for task in self.tasks:
            print(task)

    def search_tasks(self, keyword):
        return [task for task in self.tasks if keyword in task.title or keyword in task.description]

    def filter_tasks_by_status(self, status):
        return [task for task in self.tasks if task.status == status]

    def save_tasks_to_db(self):
        save_tasks_to_db(self.tasks, self.db_path)

    def load_tasks_from_db(self):
        self.tasks = load_tasks_from_db(self.db_path)