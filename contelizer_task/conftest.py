import pytest

from domain.entities.pesel_entity import PeselEntity
from domain.entities.word_prcessing_entity import WordProcessingEntity


@pytest.fixture(name="pesel_valid_entity")
def fixture_valid_pesel_entity():
    pesel = PeselEntity(number=65432101239)
    return pesel


@pytest.fixture(name="pesel_invalid_entity")
def fixture_invalid_pesel_entity():
    pesel = PeselEntity(number=65432101238)
    return pesel


@pytest.fixture(name="word_processing_valid_entity")
def fixture_valid_word_processing_entity():
    word_processing = WordProcessingEntity(content="foo bar baz 123456789")
    return word_processing
