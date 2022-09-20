
import pytest

from pynlpl.local.text.stanza import Stanza_English_default

lang_model = Stanza_English_default()


text_for_testing = "PyNLP is the universal open source NLP library for Python. It is maintained by The Text API team."

def test_stanza_sentence_segementation():
  assert lang_model.sentence_segmentation(text_for_testing) == ["PyNLP is the universal open source NLP library for Python.", "It is maintained by The Text API team."]

def test_token_segmentation():
  assert lang_model.token_segmentation(text_for_testing) == ['PyNLP', 'is', 'the', 'universal', 'open', 'source', 'NLP', 'library', 'for', 'Python', '.', 'It', 'is', 'maintained', 'by', 'The', 'Text', 'API', 'team', '.']
