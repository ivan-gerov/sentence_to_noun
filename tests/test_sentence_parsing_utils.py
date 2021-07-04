from includes.sentence_parsing_utils import SentenceParser, InvalidSentenceError

import pytest


def test_get_nouns():
    """
    Tests that SentenceParser.get_nouns method successfully
    extracts the nouns from a sentence.
    """

    test_sentence = "This is a sentence of tests."
    expected_output = ["sentence", "tests"]
    sentence_parser = SentenceParser(test_sentence)
    assert sentence_parser.get_nouns() == expected_output


def test_get_nouns_no_alphabetical():
    """
    Asserts that SentenceParser.get_nouns will raise an InvalidSentenceError
    if the sentence provided doesn't include any alphabetical characters.
    """

    test_sentence = "12312312323"
    sentence_parser = SentenceParser(test_sentence)
    with pytest.raises(InvalidSentenceError):
        sentence_parser.get_nouns()


def test_get_nouns_no_nouns():
    """
    Asserts that SentenceParser.get_nouns will raise an InvalidSentenceError
    if the sentence provided doesn't include any nouns.
    """

    test_sentence = "I am"
    sentence_parser = SentenceParser(test_sentence)
    with pytest.raises(InvalidSentenceError):
        sentence_parser.get_nouns()
