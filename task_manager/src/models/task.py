class Task:
    def __init__(self, task_id, title, description, status="не выполнено"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.status = status

    def __str__(self):
        return f"ID: {self.task_id}, Title: {self.title}, Description: {self.description}, Status: {self.status}"