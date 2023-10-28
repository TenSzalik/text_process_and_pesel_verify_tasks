import pytest

from domain.entities.word_prcessing_entity import WordProcessingEntity
from domain.managers.word_processing_manager import WordProcessingManager


def test_create_word_processing_manager(word_processing_valid_entity):
    """ Responsible for testing creation of WordProcessingManager
    """
    word_processing_entity = WordProcessingEntity(word_processing_valid_entity.content)
    word_processing_manager = WordProcessingManager(word_processing_entity)
    assert callable(word_processing_manager.shuffle_content)


@pytest.mark.parametrize(
    "word, expected_length",
    [
        ("a", 1),
        ("apple", 5),
        ("testing", 7),
    ],
)
def test_word_processing_shuffle_word(word, expected_length):
    """ Responsible for checking whether one single word was shuffled.
    The first and last letter in each word should not be shuffled.
    """
    shuffled = WordProcessingManager.shuffle_word(word)
    assert len(shuffled) == expected_length
    if len(shuffled) <= 3:
        assert shuffled == word
    else:
        assert shuffled != word
        assert shuffled[0] == word[0]
        assert shuffled[-1] == word[-1]


@pytest.mark.parametrize(
    "text",
    [
        ("a"),
        ("ab"),
        ("abc"),
        ("abcd"),
        ("abcde"),
        ("abcdefghijklmnopqrstuvwxyz !@#$%^&*()_+{}|:<>'?~\n"),
        ("\n!@#$%^&* \n()_+{}|:<>'?~"),
        ("This is regular, representative tekst for test."),
    ],
)
def test_word_processing_shuffle_content(text):
    """ Responsible for checking whether content was shuffled.
    The first and last letter in each word should not be shuffled.
    """
    word_processing = WordProcessingEntity(text)
    manager = WordProcessingManager(word_processing)
    shuffled_text = manager.shuffle_content()

    word_processing_array = word_processing.content.split(" ")
    shuffled_array = shuffled_text.split(" ")

    assert len(word_processing_array) == len(shuffled_array)

    for index, word in enumerate(word_processing_array):
        if len(word) <= 3:
            assert word == shuffled_array[index]
        else:
            assert word != shuffled_array[index]
            if word[0] == "\n":
                """New line ('\n') is in default removed from string
                """
                assert word[1] == shuffled_array[index][0]
            elif word[-1] == "\n":
                assert word[-2] == shuffled_array[index][-1]
            else:
                pass
