from django.urls import reverse


def test_get(client):
    url = reverse("home")
    resp = client.get(url)
    assert 200 == resp.status_code
