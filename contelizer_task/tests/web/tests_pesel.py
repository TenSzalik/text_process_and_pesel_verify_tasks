from django.urls import reverse
import pytest


def test_send_valid_pesel_form(client, pesel_valid_entity):
    pesel_data = pesel_valid_entity.number
    response = client.post(reverse("pesel"), {"pesel": pesel_data})

    assert response.status_code == 200
    assert "pesel_validator_result.html" in [
        template.name for template in response.templates
    ]
    assert "Data: 1965-03-21" in response.content.decode("utf-8")
    assert "gender: male" in response.content.decode("utf-8")


def test_send_invalid_pesel_form(client, pesel_invalid_entity):
    pesel_data = pesel_invalid_entity.number
    response = client.post(reverse("pesel"), {"pesel": pesel_data})

    assert response.status_code == 400
    assert "Data:" not in response.content.decode("utf-8")
    assert "gender:" not in response.content.decode("utf-8")
    assert "Invalid PESEL" in response.content.decode("utf-8")
