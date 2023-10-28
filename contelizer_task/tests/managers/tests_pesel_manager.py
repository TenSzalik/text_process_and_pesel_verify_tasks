from datetime import date

import pytest

from domain.managers.pesel_manager import PeselManager


def test_create_pesel_manager(pesel_valid_entity):
    """Responsible for testing creation of PeselManager"""
    pesel_manager = PeselManager(pesel=pesel_valid_entity)
    assert callable(pesel_manager.is_valid)
    assert callable(pesel_manager.get_birth_date)
    assert callable(pesel_manager.get_gender)


def test_pesel_is_valid(pesel_valid_entity):
    pesel_manager = PeselManager(pesel=pesel_valid_entity)
    assert pesel_manager.is_valid()


def test_pesel_is_invalid(pesel_invalid_entity):
    pesel_manager = PeselManager(pesel=pesel_invalid_entity)
    assert not pesel_manager.is_valid()


def test_pesel_get_birth_date(pesel_valid_entity):
    pesel_manager = PeselManager(pesel=pesel_valid_entity)
    assert pesel_manager.get_birth_date() == date(1965, 3, 21)


def test_pesel_get_gender(pesel_valid_entity):
    pesel_manager = PeselManager(pesel=pesel_valid_entity)
    assert pesel_manager.get_gender() == "male"
