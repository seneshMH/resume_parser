from django.test.client import Client
from django.urls import reverse

def test_home(client : Client):
    url = reverse("home_page")
    response = client.get(url)
    assert response.status_code == 200
    assert b"Resume Parser" in response.content