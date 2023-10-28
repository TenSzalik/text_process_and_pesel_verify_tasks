import pytest


def test_main_page_exist(client):
    response = client.get('/')
    assert response.status_code == 200
    assert [template.name for template in response.templates] == ["main.html"]

    response_content = response.content.decode("utf-8")
    assert "Contelizer app" in response_content
    assert "Text file processing" in response_content
    assert "PESEL number validation" in response_content
