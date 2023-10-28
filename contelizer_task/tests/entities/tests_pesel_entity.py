import pytest

from domain.entities.pesel_entity import PeselEntity


def test_create_pesel_entity(pesel_valid_entity):
    pesel = PeselEntity(number=pesel_valid_entity.number)
    assert pesel.number == pesel_valid_entity.number
