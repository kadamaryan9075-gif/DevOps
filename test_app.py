import unittest
from app import app, tasks


class TodoAppTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        tasks.clear()

    def test_home_page_loads(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"My To-Do List", response.data)

    def test_add_task(self):
        response = self.client.post("/add", data={"title": "Study Python"})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["title"], "Study Python")

    def test_blank_task_is_not_added(self):
        self.client.post("/add", data={"title": "   "})
        self.assertEqual(len(tasks), 0)

    def test_complete_and_delete_task(self):
        self.client.post("/add", data={"title": "Test DevOps"})
        task_id = tasks[0]["id"]
        self.client.post(f"/complete/{task_id}")
        self.assertTrue(tasks[0]["done"])
        self.client.post(f"/delete/{task_id}")
        self.assertEqual(len(tasks), 0)


if __name__ == "__main__":
    unittest.main()
