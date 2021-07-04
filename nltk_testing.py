from includes.constants import NLTK_DATA
import os
import re
import nltk

nltk.data.path.append(NLTK_DATA) 

from nltk.tokenize import WordPunctTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


sentences = [
    "The question is in a way meaningless, she knows, but one must ask",
    "Love in such situations is rarely real, love",
    "Sex is the engine, exalting and ruining people, sex and frustration",
    "Love is what people believe is worth the path of devastation",
    "This is 3",
    "33333333333333",
    "Blah blah blah blaaaah",
    "YES MAN",
    "MASM       DAMSDM           ",
]


def get_nouns1(sentence):
    noun_positions = ["NN", "NNS", "NNP", "NNPS", "N"]
    is_noun = lambda pos: pos in noun_positions
    tokenized = WordPunctTokenizer().tokenize(sentence)
    nouns = (word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos))
    return list(nouns)


def get_nouns2(sentence):
    word_punct_token = WordPunctTokenizer().tokenize(sentence)

    clean_tokens = []
    for token in word_punct_token:
        token = token.lower()

        # remove any value that are not alphabetical
        new_token = re.sub(r"[^a-zA-Z]+", "", token)

        # remove empty value and single character value
        if new_token != "" and len(new_token) >= 2:
            vowels = len([v for v in new_token if v in "aeiou"])
            if vowels != 0:  # remove line that only contains consonants
                clean_tokens.append(new_token)

    noun_types = ["NN", "NNS", "NNP", "NNPS", "N"]
    is_noun = lambda pos: pos in noun_types
    nouns = [word for (word, pos) in nltk.pos_tag(clean_tokens) if is_noun(pos)]
    return nouns


for s in sentences:
    print(f"{get_nouns1(s)} ---> \n{get_nouns2(s)}\n\n")

