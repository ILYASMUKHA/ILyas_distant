import sqlite3
from src.models.task import Task

def save_tasks_to_db(tasks, db_path='tasks.db'):
    """
    Сохраняет задачи в базу данных.
    :param tasks: Список задач.
    :param db_path: Путь к базе данных (по умолчанию 'tasks.db').
    """
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (id INTEGER PRIMARY KEY, title TEXT, description TEXT, status TEXT)''')
    c.execute("DELETE FROM tasks")  # Очищаем таблицу перед сохранением
    for task in tasks:
        c.execute("INSERT INTO tasks VALUES (?, ?, ?, ?)",
                  (task.task_id, task.title, task.description, task.status))
    conn.commit()
    conn.close()

def load_tasks_from_db(db_path='tasks.db'):
    """
    Загружает задачи из базы данных.
    :param db_path: Путь к базе данных (по умолчанию 'tasks.db').
    :return: Список задач.
    """
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (id INTEGER PRIMARY KEY, title TEXT, description TEXT, status TEXT)''')
    c.execute("SELECT * FROM tasks")
    rows = c.fetchall()
    tasks = [Task(row[0], row[1], row[2], row[3]) for row in rows]
    conn.close()
    return tasks