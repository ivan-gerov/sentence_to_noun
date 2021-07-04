
import re
import nltk

from nltk.tokenize import WordPunctTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

class SentenceParser:
    """Object representing a sentence."""

    def __init__(self, sentence_string):        
        self.sentence_string = sentence_string

    @staticmethod
    def get_nouns(sentence):
        word_punct_token = WordPunctTokenizer().tokenize(sentence)

        clean_tokens=[]
        for token in word_punct_token:
            token = token.lower()

            # remove any value that are not alphabetical
            new_token = re.sub(r'[^a-zA-Z]+', '', token)

            # remove empty value and single character value
            if new_token != "" and len(new_token) >= 2: 
                vowels=len([v for v in new_token if v in "aeiou"])
                if vowels != 0: # remove line that only contains consonants
                    clean_tokens.append(new_token)

        noun_types = ['NN','NNS','NNP','NNPS', 'N']
        is_noun = lambda pos: pos in noun_types
        nouns = [word for (word, pos) in nltk.pos_tag(clean_tokens) if is_noun(pos)]
        
        if nouns:
            return nouns
        else:
            raise InvalidSentenceError(sentence)


class InvalidSentenceError(Exception):
    """Exception raised for sentences which are not valid"""

    def __init__(self, sentence_string, message="The sentence you have provided is invalid"):
        self.sentence_string = sentence_string
        self.message = message

        super().__init__(self.message)

    def __str__(self):
        return f"{self.sentence_string} -> {self.message}."
