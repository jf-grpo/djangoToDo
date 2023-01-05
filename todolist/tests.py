# todolist/tests.py
'''
import datetime
from django.test import TestCase, Client
from django.http import HttpResponse
from django.urls import reverse

from todolist.models import TaskList

# Create your tests here.

class TestTaskListModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Creates a task instance that our tests can access.
        setUpTestData is executed once, so our task instance is
        shared between tests.
        """
        cls.task_name = "Book dentist appointment"
        cls.task = TaskList.objects.create(name=cls.task_name)
 
    def test_task_name(self):
        self.assertEqual(self.task.name, self.task_name)
 
    def test_task_default_status(self):
        """Test that our task was assigned a status of 'To Do'"""
 
        expected = TaskList.StatusChoice.TODO
        actual = self.task.status
 
        self.assertEqual(expected, actual)
 
    def test_task_created(self):
        """Tests that task.created stores a datetime"""
 
        self.assertEqual(type(self.task.created), datetime.datetime)
 
    def test_str(self):
        expected = f"To do: {self.task_name}"
        actual = str(self.task)
 
        self.assertEqual(expected, actual)
'''

# todolist/tests.py
 
import datetime
 
from django.db.models import QuerySet
from django.http import HttpResponse
from django.urls import reverse
from django.test import TestCase, Client
 
from todolist.models import TaskList
 
class TestTaskListModel(TestCase):
     ...
 
class TestIndexView(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse("index")
        cls.client = Client()
        cls.task = TaskList.objects.create(name="book dentist appointment")
 
    def test_index_view_returns_httpresponse(self):
        """Test our view returns a HttpResponse"""
 
        response = self.client.get(self.url)
 
        self.assertTrue(isinstance(response, HttpResponse))
 
    def test_status_code(self):
        response = self.client.get(self.url)
 
        self.assertEqual(response.status_code, 200)
 
    def test_context(self):
        """Tests the context contains queryset of tasks"""
        response = self.client.get(self.url)
 
        self.assertIn("tasks", response.context)
 
        tasks = response.context["tasks"]
 
        self.assertTrue(isinstance(tasks, QuerySet))
        self.assertEqual(tasks.first(), self.task)
 
    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "temp_index.html")

class TestDeleteTaskView(TestCase):
    def setUp(self):
        self.task = TaskList.objects.create(name="Book dentist appointment")
        self.client = Client()
 
    def test_delete_task(self):
        url = reverse("delete", args=[self.task.id])
 
        response = self.client.get(url)
 
        self.assertEqual(response.status_code, 302)
 
    def test_delete_task_deletes_task(self):
        url = reverse("delete", args=[self.task.id])
 
        self.assertEqual(TaskList.objects.count(), 1)
 
        self.client.get(url)
 
        self.assertEqual(TaskList.objects.count(), 0)
 
    def test_delete_task_raises_404(self):
        bad_id = 999
        self.assertFalse(TaskList.objects.filter(id=bad_id).exists())
 
        url = reverse("delete", args=[bad_id])
 
        response = self.client.get(url)
 
        self.assertEqual(response.status_code, 404)