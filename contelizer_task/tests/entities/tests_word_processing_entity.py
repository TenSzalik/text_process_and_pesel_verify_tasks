import pytest

from domain.entities.word_prcessing_entity import WordProcessingEntity


def test_create_word_processing_entity(word_processing_valid_entity):
    """ Responsible for testing creation of WordProcessingEntity
    """
    word_processing = WordProcessingEntity(content=word_processing_valid_entity.content)
    assert word_processing.content == word_processing_valid_entity.content
