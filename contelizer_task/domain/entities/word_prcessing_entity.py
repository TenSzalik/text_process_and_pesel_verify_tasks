from dataclasses import dataclass
from typing import Union


@dataclass
class WordProcessingEntity:
    """
    :param content: content to shuffle
    :param loose: If true, shuffle the content without checking whether
        the shuffled word is the same as the original one. With loose=True
        it's probably to get the same output like input. It's experimental
        param - NOT implemented in tests.
    """
    content: Union[str, bytes]
    loose: bool = False
