import unittest
import os
from src.managers.task_manager import TaskManager

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        """
        Настройка перед каждым тестом.
        """
        # Используем временную базу данных для тестов
        self.db_path = 'test_tasks.db'
        self.manager = TaskManager(db_path=self.db_path)

    def tearDown(self):
        """
        Очистка после каждого теста.
        """
        # Удаляем временную базу данных после тестов
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

    def test_add_task(self):
        """
        Тест добавления задачи.
        """
        self.manager.add_task("Test Task", "This is a test task")
        self.assertEqual(len(self.manager.tasks), 1)

    def test_delete_task(self):
        """
        Тест удаления задачи.
        """
        self.manager.add_task("Test Task", "This is a test task")
        self.manager.delete_task(1)
        self.assertEqual(len(self.manager.tasks), 0)

    def test_update_task_status(self):
        """
        Тест изменения статуса задачи.
        """
        self.manager.add_task("Test Task", "This is a test task")
        self.manager.update_task_status(1, "в процессе")
        task = self.manager.tasks[0]
        self.assertEqual(task.status, "в процессе")

if __name__ == '__main__':
    unittest.main()