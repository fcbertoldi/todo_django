from rest_framework import status
from rest_framework.test import APITestCase
from .models import Task


class TaskTest(APITestCase):
    def setUp(self):
        self.base_url = '/api/task/'
        self.title = 'Cortar grama.'

    def create_task(self):
        payload = {'title': self.title}
        res = self.client.post(self.base_url, payload, format='json')
        self.assertEqual(status.HTTP_201_CREATED, res.status_code)
        return res

    def test_get_all_tasks(self):
        self.create_task()
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, self.title)
        self.assertEqual(Task.objects.get().state, 'T')

    def test_retrieve_task(self):
        create_res = self.create_task()
        task = Task.objects.get()

        expected_data = {
            'id': task.id,
            'title': task.title,
            'description': None,
            'state': 'T'
        }

        retrieve_res = self.client.get(self.base_url+str(create_res.data['id']))
        self.assertEqual(status.HTTP_200_OK, retrieve_res.status_code)
        self.assertEqual(expected_data, retrieve_res.data)

    def test_delete_task(self):
        create_res = self.create_task()
        delete_res = self.client.delete(self.base_url+str(create_res.data['id']))
        self.assertEqual(status.HTTP_204_NO_CONTENT, delete_res.status_code)

    def test_change_state(self):
        create_res = self.create_task()
        new_state = 'S'
        payload = {'title': self.title, 'state': new_state}
        put_res = self.client.put(self.base_url+str(create_res.data['id']), payload, format='json')
        self.assertEqual(status.HTTP_200_OK, put_res.status_code)
        task = Task.objects.get()
        self.assertEqual(new_state, task.state)

    def test_archive_task(self):
        create_res = self.create_task()
        archive_res = self.client.get(self.base_url+str(create_res.data['id'])+'/archive')
        self.assertEqual(status.HTTP_200_OK, archive_res.status_code)

        task = Task.objects.get()
        expected_data = {
            'id': task.id,
            'title': task.title,
            'description': None,
            'state': 'T'
        }
        archived_res = self.client.get('/api/archived/'+str(create_res.data['id']))
        self.assertEqual(status.HTTP_200_OK, archived_res.status_code)
        self.assertEqual(expected_data, archived_res.data)

