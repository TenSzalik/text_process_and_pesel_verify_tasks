from dataclasses import dataclass
from typing import Union


@dataclass
class PeselEntity:
    """Definition of the Pesel entity
    """
    number: Union[str, int]
