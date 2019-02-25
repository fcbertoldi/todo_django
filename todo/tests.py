from rest_framework import status
from rest_framework.test import APITestCase
from .models import Task


class TaskTest(APITestCase):
    def setUp(self):
        self.task_url = '/api/task'
        self.archived_url = '/api/archived'
        self.title = 'Cortar grama.'

    def create_task(self):
        payload = {'title': self.title}
        res = self.client.post(self.task_url, payload, format='json')
        self.assertEqual(status.HTTP_201_CREATED, res.status_code)
        return res

    def archive_task(self, task_id):
        archive_res = self.client.post('/'.join((self.task_url, str(task_id), 'archive')))
        self.assertEqual(status.HTTP_200_OK, archive_res.status_code)
        return archive_res

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
            'state': 'TODO'
        }

        retrieve_res = self.client.get(self.task_url + '/' + str(create_res.data['id']))
        self.assertEqual(status.HTTP_200_OK, retrieve_res.status_code)
        self.assertEqual(expected_data, retrieve_res.data)

    def test_retrieve_invalid_task(self):
        retrieve_res = self.client.get(self.task_url+'/1')
        self.assertEqual(status.HTTP_404_NOT_FOUND, retrieve_res.status_code)

    def test_delete_task(self):
        create_res = self.create_task()
        delete_res = self.client.delete(self.task_url + '/' + str(create_res.data['id']))
        self.assertEqual(status.HTTP_204_NO_CONTENT, delete_res.status_code)

    def test_change_state(self):
        create_res = self.create_task()
        new_state = 'STARTED'
        payload = {'title': self.title, 'state': new_state}
        put_res = self.client.put(self.task_url + '/' + str(create_res.data['id']), payload, format='json')
        self.assertEqual(status.HTTP_200_OK, put_res.status_code)
        task = Task.objects.get()
        self.assertEqual('S', task.state)

    def test_archive_task(self):
        create_res = self.create_task()
        task_id = create_res.data['id']
        self.archive_task(task_id)

        task = Task.objects.get()
        expected_data = {
            'id': task.id,
            'title': task.title,
            'description': None,
            'state': 'TODO'
        }

        archived_res = self.client.get('/'.join((self.archived_url, str(task_id))))
        self.assertEqual(status.HTTP_200_OK, archived_res.status_code)
        self.assertEqual(expected_data, archived_res.data)

        task_res = self.client.get(self.task_url+'/'+str(task_id))
        self.assertEqual(status.HTTP_404_NOT_FOUND, task_res.status_code)

    def test_retrieve_invalid_archived_task(self):
        create_res = self.create_task()
        task_id = create_res.data['id']
        res = self.client.get(self.archived_url+'/'+str(task_id))
        self.assertEqual(status.HTTP_404_NOT_FOUND, res.status_code)

    def test_unarchive_task(self):
        create_res = self.create_task()
        task_id = create_res.data['id']
        self.archive_task(task_id)
        unarchive_res = self.client.post('/'.join((self.archived_url, str(task_id), 'unarchive')))
        self.assertEqual(status.HTTP_200_OK, unarchive_res.status_code)

        unarchived_res = self.client.get('/'.join((self.archived_url, str(task_id))))
        self.assertEqual(status.HTTP_404_NOT_FOUND, unarchived_res.status_code)

        task_res = self.client.get('/'.join((self.task_url, str(task_id))))
        self.assertEqual(status.HTTP_200_OK, task_res.status_code)
