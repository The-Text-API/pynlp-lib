
import pytest

from pynlpl.local.text.stanza_api import Stanza_English_default

lang_model = Stanza_English_default()


text_for_testing = "PyNLP is the universal open source NLP library for Python. It is maintained by The Text API team."

def test_stanza_sentence_segementation():
  assert lang_model.sentence_segmentation(text_for_testing) == ["PyNLP is the universal open source NLP library for Python.", "It is maintained by The Text API team."]

def test_token_segmentation():
  assert lang_model.token_segmentation(text_for_testing) == ['PyNLP', 'is', 'the', 'universal', 'open', 'source', 'NLP', 'library', 'for', 'Python', '.', 'It', 'is', 'maintained', 'by', 'The', 'Text', 'API', 'team', '.']

def test_pos_tagging():
  assert lang_model.pos_tagging(text_for_testing) == ['WORD: PyNLP, UPOS: PROPN, XPOS: NNP ', 'WORD: is, UPOS: AUX, XPOS: VBZ ', 'WORD: the, UPOS: DET, XPOS: DT ', 'WORD: universal, UPOS: ADJ, XPOS: JJ ', 'WORD: open, UPOS: ADJ, XPOS: JJ ', 'WORD: source, UPOS: NOUN, XPOS: NN ', 'WORD: NLP, UPOS: NOUN, XPOS: NN ', 'WORD: library, UPOS: NOUN, XPOS: NN ', 'WORD: for, UPOS: ADP, XPOS: IN ', 'WORD: Python, UPOS: PROPN, XPOS: NNP ', 'WORD: ., UPOS: PUNCT, XPOS: . ', 'WORD: It, UPOS: PRON, XPOS: PRP ', 'WORD: is, UPOS: AUX, XPOS: VBZ ', 'WORD: maintained, UPOS: VERB, XPOS: VBN ', 'WORD: by, UPOS: ADP, XPOS: IN ', 'WORD: The, UPOS: DET, XPOS: DT ', 'WORD: Text, UPOS: PROPN, XPOS: NNP ', 'WORD: API, UPOS: PROPN, XPOS: NNP ', 'WORD: team, UPOS: NOUN, XPOS: NN ', 'WORD: ., UPOS: PUNCT, XPOS: . ']

def test_text_lemmatization():
  assert lang_model.text_lemmatization(text_for_testing) == ['WORD: PyNLP, LEMMA: PyNLP ', 'WORD: is, LEMMA: be ', 'WORD: the, LEMMA: the ', 'WORD: universal, LEMMA: universal ', 'WORD: open, LEMMA: open ', 'WORD: source, LEMMA: source ', 'WORD: NLP, LEMMA: nlp ', 'WORD: library, LEMMA: library ', 'WORD: for, LEMMA: for ', 'WORD: Python, LEMMA: python ', 'WORD: ., LEMMA: . ', 'WORD: It, LEMMA: it ', 'WORD: is, LEMMA: be ', 'WORD: maintained, LEMMA: maintain ', 'WORD: by, LEMMA: by ', 'WORD: The, LEMMA: the ', 'WORD: Text, LEMMA: text ', 'WORD: API, LEMMA: api ', 'WORD: team, LEMMA: team ', 'WORD: ., LEMMA: . ']

def test_dependency_parsing():
  assert lang_model.dependency_parsing(text_for_testing) == ['ID: 1, WORD: PyNLP, THREAD ID: 8, THREAD: library, DEPREL: nsubj ', 'ID: 2, WORD: is, THREAD ID: 8, THREAD: library, DEPREL: cop ', 'ID: 3, WORD: the, THREAD ID: 8, THREAD: library, DEPREL: det ', 'ID: 4, WORD: universal, THREAD ID: 8, THREAD: library, DEPREL: amod ', 'ID: 5, WORD: open, THREAD ID: 8, THREAD: library, DEPREL: amod ', 'ID: 6, WORD: source, THREAD ID: 8, THREAD: library, DEPREL: compound ', 'ID: 7, WORD: NLP, THREAD ID: 8, THREAD: library, DEPREL: compound ', 'ID: 8, WORD: library, THREAD ID: 0, THREAD: root, DEPREL: root ', 'ID: 9, WORD: for, THREAD ID: 10, THREAD: Python, DEPREL: case ', 'ID: 10, WORD: Python, THREAD ID: 8, THREAD: library, DEPREL: nmod ', 'ID: 11, WORD: ., THREAD ID: 8, THREAD: library, DEPREL: punct ', 'ID: 1, WORD: It, THREAD ID: 3, THREAD: maintained, DEPREL: nsubj:pass ', 'ID: 2, WORD: is, THREAD ID: 3, THREAD: maintained, DEPREL: aux:pass ', 'ID: 3, WORD: maintained, THREAD ID: 0, THREAD: root, DEPREL: root ', 'ID: 4, WORD: by, THREAD ID: 8, THREAD: team, DEPREL: case ', 'ID: 5, WORD: The, THREAD ID: 8, THREAD: team, DEPREL: det ', 'ID: 6, WORD: Text, THREAD ID: 8, THREAD: team, DEPREL: compound ', 'ID: 7, WORD: API, THREAD ID: 8, THREAD: team, DEPREL: compound ', 'ID: 8, WORD: team, THREAD ID: 3, THREAD: maintained, DEPREL: obl ', 'ID: 9, WORD: ., THREAD ID: 3, THREAD: maintained, DEPREL: punct ']
