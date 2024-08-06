from django.test import TestCase
from .models import Task
from rest_framework.test import APIClient

# Create your tests here.
class Testing(TestCase):
    fixtures = ['initial_tasks.json']

    def setUp(self):
        """
        The setUp method is called before each test method runs. It's used to set up any state or objects needed for the tests.
        """
        #This client will be used to make requests to your API endpoints during the tests.
        self.client = APIClient()

    def test_get_task(self):
        response = self.client.get('/api/tasks/')
        tasks = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(tasks[0]['id'], 1)
        print(tasks)

    def test_add_task(self):
          
        task_data = {
        'taskid' : 2,
        'title' : "Sample 2",
        'completed' : False,
    }

        response = self.client.post('/api/tasks/add/', task_data, format='json')

        # Verify the response status code
        self.assertEqual(response.status_code, 200)

        # Verify the response data
        task = response.json()
        tasks = Task.objects.all()
        for t in tasks:
            print(t.taskid, t.title, t.completed)
        self.assertEqual(task['title'], task_data['title'])


    def test_update_task(self):
        task_data = {
        'taskid' : 1,
        'title' : "Sample Task 1 updated",
        'completed' : True,
    }   

        taskid = 1
        response = self.client.put(f'/api/tasks/update/{taskid}/', task_data, format='json')

        updated_task = response.json()
        print("Updated task data: ", updated_task)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(updated_task['title'], task_data['title'])

    def test_delete_task(self):
        taskid = 1
        response = self.client.delete(f'/api/tasks/delete/{taskid}/', format='json')

        tasks = Task.objects.all()
        for t in tasks:
            print(t.taskid, t.title, t.completed)
        self.assertEqual(response.status_code, 200)


        



