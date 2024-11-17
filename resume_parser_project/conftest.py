from django.test.client import Client
import pytest

@pytest.fixture
def Client():
   return Client()