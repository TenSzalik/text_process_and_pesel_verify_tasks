from django.urls import reverse
import pytest


def test_send_valid_pesel_form(client, pesel_valid_entity):
    pesel_data = pesel_valid_entity.number
    response = client.post(reverse("pesel"), {"pesel": pesel_data})

    assert response.status_code == 200
    assert "pesel/pesel_validator_result.html" in [
        template.name for template in response.templates
    ]
    response_content = response.content.decode("utf-8")
    assert "Data: 1965-03-21" in response_content
    assert "gender: male" in response_content


def test_send_invalid_pesel_form(client, pesel_invalid_entity):
    pesel_data = pesel_invalid_entity.number
    response = client.post(reverse("pesel"), {"pesel": pesel_data})
    # breakpoint()
    assert response.status_code == 400
    assert response.templates == []

    response_content = response.content.decode("utf-8")
    assert "Data:" not in response_content
    assert "gender:" not in response_content
    assert "Invalid PESEL" in response_content
