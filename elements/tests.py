from typing import Any
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class ElementsViewSetTest(TestCase):
    """
    Class to test list filtered and creation of Elements
    """
    def setUp(self):
        self.client = APIClient()
        self.status = 60
        self.name = "Element Test"
        self.wrong_status = "text"
    

    def test_list_ok(self):
        response = self.client.get(
            f'/elements/?status={self.status}', format="json"
        )
        self.assertEquals(status.HTTP_200_OK, response.status_code)
    
    def test_filter_not_ok(self):
        response = self.client.get(
            f'/elements/?status={self.wrong_status}', format="json"
        )
        self.assertEquals(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertEquals(["status"], list(response.data.keys()))
    
    def test_create_ok(self):
        response = self.client.post(
            f'/elements/', dict(status=self.status, name=self.name),format="json"
        )
        self.assertEquals(status.HTTP_201_CREATED, response.status_code)
