from abc import ABC, abstractmethod
from datetime import date


class PeselInterface(ABC):
    """ Interface of the PeselManager
    """
    @abstractmethod
    def is_valid(self) -> bool:
        pass

    @abstractmethod
    def get_birth_date(self) -> date:
        pass

    @abstractmethod
    def get_gender(self) -> str:
        pass
