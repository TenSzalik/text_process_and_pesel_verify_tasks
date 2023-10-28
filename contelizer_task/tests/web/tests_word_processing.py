from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
import pytest


@pytest.mark.parametrize(
    "text",
    [
        (b"a"),
        (b"ab"),
        (b"abc"),
        (b"abcd"),
        (b"abcde"),
        (b"abcdefghijklmnopqrstuvwxyz !@#$%^&*()_+{}|:<>'?~\n"),
        (b"\n!@#$%^&* \n()_+{}|:<>'?~"),
        (b"This is regular, representative tekst for test."),
    ],
)
def test_send_word_processing_form_loose_false(client, text):
    file_data = text
    file_data_array = file_data.decode().split(" ")
    response = client.post(
        reverse("process_text"), {"content": SimpleUploadedFile("test.txt", file_data)}
    )
    assert response.status_code == 200

    shuffled_array = response.content.decode()
    shuffled_array = shuffled_array.split(" ")

    assert len(file_data_array) == len(shuffled_array)

    for index, word in enumerate(file_data_array):
        if len(word) <= 3:
            assert word == shuffled_array[index]
        else:
            assert word != shuffled_array[index]
            if word[0] == "\n":
                assert word[1] == shuffled_array[index][0]
            elif word[-1] == "\n":
                assert word[-2] == shuffled_array[index][-1]
            else:
                pass
