from abc import ABC, abstractmethod


class WordProcessingInterface(ABC):
    """ Interface of the WordProcessingManager
    """
    @abstractmethod
    def shuffle_content(self) -> str:
        pass
