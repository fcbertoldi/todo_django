from rest_framework import status
from rest_framework.test import APITestCase
from .models import Task


class TaskTest(APITestCase):
    def test_get_all_tasks(self):
        url = '/task/'
        payload = {'title': 'Cortar grama.'}
        response = self.client.post(url, payload, format='json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
