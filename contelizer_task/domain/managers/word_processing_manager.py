import re

from more_itertools import random_permutation

from domain.entities.word_prcessing_entity import WordProcessingEntity
from domain.interfaces.word_processing_interface import WordProcessingInterface


class WordProcessingManager(WordProcessingInterface):
    """ Responsible for processing text
    """
    def __init__(self, word_processing: WordProcessingEntity) -> None:
        if isinstance(word_processing.content, bytes):
            self.content = word_processing.content.decode()
        else:
            self.content = word_processing.content
        self.loose = word_processing.loose

    @staticmethod
    def shuffle_word(word: str, loose: bool = False) -> str:
        if len(word) <= 3:
            return word

        shuffled = "".join(random_permutation(word[1:-1]))
        if loose is False:
            while word[1:-1] == shuffled:
                shuffled = "".join(random_permutation(word[1:-1]))

        shuffled_word = f"{ word[0] }{ shuffled }{ word[-1] }"
        return shuffled_word

    def shuffle_content(self) -> str:
        splitted_text = re.split(r" |\n", self.content)
        splitted_text = list(filter(None, splitted_text))
        text_array = []
        for word in splitted_text:
            text_array.append(self.shuffle_word(word, self.loose))
        modified_text = " ".join(text_array)
        return modified_text
