from datetime import date

from domain.entities.pesel_entity import PeselEntity
from domain.interfaces.pesel_interface import PeselInterface


class PeselManager(PeselInterface):
    """ Pesel class to serve PESEL number
    """
    def __init__(self, pesel: PeselEntity):
        self.pesel = str(pesel.number)

    def is_valid(self) -> bool:
        WEIGHTS = (1, 3, 7, 9, 1, 3, 7, 9, 1, 3)
        control_sum = 0

        if not self.pesel.isdigit():
            return False
        if not len(self.pesel) == 11:
            return False
        for i in range(10):
            control_sum += int(self.pesel[i]) * WEIGHTS[i]
        control_digit = (10 - (control_sum % 10)) % 10

        if control_digit == int(self.pesel[10]):
            return True

    def get_birth_date(self) -> date | ValueError:
        year = int(self.pesel[0:2])
        month = int(self.pesel[2:4])
        day = int(self.pesel[4:6])

        century = {
            80: 1800,
            0: 1900,
            20: 2000,
            40: 2100,
            60: 2200,
        }

        year += century.get(month, 1900)
        month %= 20

        try:
            birth_date = date(year, month, day)
            return birth_date
        except ValueError as error:
            return error

    def get_gender(self) -> str:
        return "male" if int(self.pesel[-2]) % 2 else "female"
